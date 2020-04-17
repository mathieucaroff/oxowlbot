import logging
import os
from typing import Any, Callable, List

from .answer import Answer, AnswerEngine
from .ontology import Ontology
from .parsing.pword import PWord
from .parsing.stanzaProvider import createStanzaLocalPipeline, createStanzaWebPipeline

# from .parsing import Parser, ParseResult
from .util.redirect import redirect_stderr
from typing_extensions import Awaitable

with redirect_stderr():
    from owlready2 import get_ontology, default_world


class Questionbot:
    parse: List[Callable[[str], Awaitable[List[List[PWord]]]]]
    ontology: Ontology
    engine: AnswerEngine

    def __init__(self):
        # Parser engine, stanza

        if os.environ.get("STANZA_PROVIDER", None) == "web":
            logging.info("Using stanza web provider")
            createStanzaPipeline = createStanzaWebPipeline
        else:
            logging.info("Running stanza locally")
            createStanzaPipeline = createStanzaLocalPipeline

        self.parser = [createStanzaPipeline()]

        # Ontology engine
        onto: Any = get_ontology("owl/littlePony.owl")
        onto.load()
        graph: Any = default_world.as_rdflib_graph()
        self.ontology = Ontology(onto, graph)

        # Answer recipe engine
        self.engine = AnswerEngine()

    async def process(self, message: str) -> Answer:
        parse_result = await self.parse[0](message)

        answer = self.engine.process(parse_result)

        return answer
