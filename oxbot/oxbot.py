"""
oxbot, entry point for the django channel consumer
"""

from typing import Any
import os

from .answer import Answer, AnswerEngine
from .ontology import Ontology
from .parsing import Parser, ParseResult
from .util.redirect import redirect_stderr
from oxbot.stanzaProvider import createStanzaLocalPipeline, createStanzaWebPipeline
import logging

with redirect_stderr():
    from owlready2 import get_ontology, default_world

# pyright: strict


class Oxbot:
    def __init__(self):
        # Parser engine, stanza

        # stanza.Pipeline will produce an output which cannot be suppressed
        # (it calls a java runtime)
        if os.environ.get("STANZA_PROVIDER", None) == "web":
            logging.info("Using stanza web provider")
            createStanzaPipeline = createStanzaWebPipeline
        else:
            logging.info("Running stanza locally")
            createStanzaPipeline = createStanzaLocalPipeline

        self.parser = Parser(stanzaPipeline=createStanzaPipeline())

        # Ontology engine
        get_ontology("owl/littlePony.owl").load()
        graph: Any = default_world.as_rdflib_graph()
        self.ontology = Ontology(graph)

        # Answer recipe engine
        self.engine = AnswerEngine()

    async def process(self, message: str) -> Answer:
        parse_result: ParseResult = await self.parser.parse(message)

        answer = self.engine.process(parse_result)

        return answer
