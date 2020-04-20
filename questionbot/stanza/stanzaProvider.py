import abc
import json
from typing import Dict, List

from aiohttp import ClientSession

from .pword import PWord

STANZA_URL = "http://devx.oxie.cc:1088"


def toPWordListList(doc: List[List[Dict]]) -> List[List[PWord]]:
    return [[PWord(**word) for word in sentence] for sentence in doc]


class StanzaPipeline:
    @abc.abstractmethod
    async def parse(self, textInput: str) -> List[List[PWord]]: ...


def createStanzaWebPipeline() -> StanzaPipeline:
    class StanzaWebPipeline(StanzaPipeline):
        async def parse(self, textInput: str) -> List[List[PWord]]:
            async with ClientSession() as session:
                async with session.post(url=STANZA_URL, data=textInput) as resp:
                    answer = await resp.json()
            result: List[List[PWord]] = toPWordListList(answer)
            return result

    return StanzaWebPipeline()


def createStanzaLocalPipeline() -> StanzaPipeline:
    import stanza

    stanza.download("en")
    # stanza.Pipeline will produce an output which cannot be suppressed since it
    # calls a java runtime
    nlp = stanza.Pipeline("en")

    class StanzaLocalPipeline(StanzaPipeline):
        async def parse(self, textInput: str) -> List[List[PWord]]:
            answer = str(nlp(textInput))
            result: List[List[PWord]] = toPWordListList(json.loads(answer))
            return result

    return StanzaLocalPipeline()


def createStanzaTryWebPipeline():
    """
    Try to use the web pipeline, defaulting to the local pipeline at the first
    error.
    """
    stanzaWebPipeline = createStanzaWebPipeline()
    stanzaPipeline = [stanzaWebPipeline]
    selectedPipeline = ["web"]

    async def stanzaTryWebPipeline(textInput: str):
        try:
            return await stanzaPipeline[0].parse(textInput)
        except:
            if selectedPipeline[0] == "local":
                raise
            else:
                selectedPipeline[0] = "local"
                stanzaPipeline[0] = createStanzaLocalPipeline()
                return await stanzaPipeline[0].parse(textInput)

    return stanzaTryWebPipeline
