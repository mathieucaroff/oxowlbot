import abc
import json
import logging
import os
from typing import Any, Dict, List

from aiohttp import ClientSession

from .pword import PWord

STANZA_WEB_URL = os.environ.get("STANZA_WEB_URL", "http://devx.oxie.cc:1088")


def toPWordListList(doc: List[List[Dict]]) -> List[List[PWord]]:
    return [[PWord(**word) for word in sentence] for sentence in doc]


class StanzaPipeline:
    @abc.abstractmethod
    async def parse(self, textInput: str) -> List[List[PWord]]:
        ...


#
# Environement based selection
#


def createStanzaPipeline():
    STANZA_PROVIDER = os.environ.get("STANZA_PROVIDER", None)

    provider = STANZA_PROVIDER
    ok = "local_only local web web_only"
    if STANZA_PROVIDER not in ok.split():
        if STANZA_PROVIDER is not None:
            logging.warn(
                f"Got [{STANZA_PROVIDER=}] but accepted values are [{ok}]"
            )
        provider = "web"

    if provider == "localonly":
        strategy = createStanzaLocalPipeline
    elif provider == "local":
        strategy = createStanzaTryLocalPipeline
    elif provider == "web":
        strategy = createStanzaTryWebPipeline
    elif provider == "webonly":
        strategy = createStanzaWebPipeline
    else:
        raise RuntimeError()

    logging.info(f"Using stanza with {provider =}")

    return strategy()


#
# Smart auto-switching wrappers
#


def createStanzaTryWebPipeline():
    """
    Try to use the web pipeline, defaulting to the local pipeline at the first
    error.
    """
    stanzaWebPipeline = createStanzaWebPipeline()
    stanzaPipeline = [stanzaWebPipeline]
    selectedPipeline = ["web"]

    class StanzaTryWebPipeline(StanzaPipeline):
        async def parse(self, textInput: str):
            try:
                return await stanzaPipeline[0].parse(textInput)
            except:
                if selectedPipeline[0] == "local":
                    raise
                else:
                    logging.info(
                        "Stanza Web Pipeline failed, switching to local"
                    )
                    selectedPipeline[0] = "local"
                    stanzaPipeline[0] = createStanzaLocalPipeline()
                    return await stanzaPipeline[0].parse(textInput)

    return StanzaTryWebPipeline()


def createStanzaTryLocalPipeline():
    """
    Try to use the local pipeline, defaulting to the web pipeline at the first
    error.
    """
    stanzaLocalPipeline = createStanzaLocalPipeline()
    stanzaPipeline = [stanzaLocalPipeline]
    selectedPipeline = ["local"]

    class StanzaTryLocalPipeline(StanzaPipeline):
        async def parse(textInput: str):
            try:
                return await stanzaPipeline[0].parse(textInput)
            except:
                if selectedPipeline[0] == "web":
                    raise
                else:
                    logging.info(
                        "Stanza local Pipeline failed, switching to web"
                    )
                    selectedPipeline[0] = "web"
                    stanzaPipeline[0] = createStanzaWebPipeline()
                    return await stanzaPipeline[0].parse(textInput)

    return StanzaTryLocalPipeline()


#
# Base implementations
#


def createStanzaWebPipeline() -> StanzaPipeline:
    class StanzaWebPipeline(StanzaPipeline):
        async def parse(self, textInput: str) -> List[List[PWord]]:
            async with ClientSession() as session:
                async with session.post(
                    url=STANZA_WEB_URL, data=textInput
                ) as resp:
                    answer = await resp.json()
            result: List[List[PWord]] = toPWordListList(answer)
            return result

    return StanzaWebPipeline()


def createStanzaLocalPipeline() -> StanzaPipeline:
    import importlib

    stanza: Any = importlib.import_module("stanza")

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
