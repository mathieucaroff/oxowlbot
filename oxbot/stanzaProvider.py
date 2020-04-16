import json
from typing import Dict, List

from aiohttp import ClientSession

from .datatype.pword import PWord

STANZA_URL = "http://devx.oxie.cc:1088"


def toPWordListList(doc: List[List[Dict]]) -> List[List[PWord]]:
    return [[PWord(**word) for word in sentence] for sentence in doc]


def createStanzaWebPipeline():
    async def stanzaWebPipeline(textInput: str) -> List[List[PWord]]:
        async with ClientSession() as session:
            async with session.post(url=STANZA_URL, data=textInput) as resp:
                answer = await resp.json()
        result: List[List[PWord]] = toPWordListList(answer)
        return result

    return stanzaWebPipeline


def createStanzaLocalPipeline():
    import stanza

    stanza.download("en")
    nlp = stanza.Pipeline("en")

    async def stanzaLocalPipeline(textInput: str) -> List[List[PWord]]:
        answer = str(nlp(textInput))
        result: List[List[PWord]] = toPWordListList(json.loads(answer))
        return result

    return stanzaLocalPipeline


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
            return await stanzaPipeline[0](textInput)
        except:
            if selectedPipeline[0] == "local":
                raise
            else:
                selectedPipeline[0] = "local"
                stanzaPipeline[0] = createStanzaLocalPipeline()
                return await stanzaPipeline[0](textInput)

    return stanzaTryWebPipeline
