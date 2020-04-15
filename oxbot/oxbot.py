"""
oxbot, entry point for the django channel consumer
"""

from typing import Any

import stanza
from stanza.pipeline.core import Pipeline

from .answer import Answer, AnswerEngine
from .ontology import Ontology
from .parsing import Parser, ParseResult
from .util.redirect import redirect_stderr

with redirect_stderr():
    from owlready2 import get_ontology, default_world

# pyright: strict


class Oxbot:
    def __init__(self):
        # Parser engine, stanza

        # stanza.Pipeline will produce an output which cannot be suppressed
        # (it calls a java runtime)
        pipeline: Pipeline = stanza.Pipeline("en")

        self.parser = Parser(pipeline)

        # Ontology engine
        get_ontology("owl/littlePony.owl").load()
        graph: Any = default_world.as_rdflib_graph()
        self.ontology = Ontology(graph)

        # Anser recipe engine
        self.engine = AnswerEngine()

    async def process(self, message: str) -> Answer:
        parse_result: ParseResult = self.parser.parse(message)

        answer = self.engine.process(parse_result)

        return answer
