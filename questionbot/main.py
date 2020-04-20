import logging
import os
from typing import Any

from . import answer as a
from . import lexic as lx
from . import ontology as o
from .normal.normal import Normal
from .recipe.recipeGetter import RecipeGetter
from .recipeRunner import RecipeRunner
from .stanza.stanzaProvider import (
    StanzaPipeline,
    createStanzaLocalPipeline,
    createStanzaWebPipeline,
)
from .util.log import log
from .util.redirect import redirect_stderr

with redirect_stderr():
    from owlready2 import get_ontology, default_world


class Questionbot:
    parser: StanzaPipeline
    ontology: o.Ontology
    lexic: lx.Lexic

    def __init__(self):
        # Parser engine, stanza
        createStanzaPipeline: Any

        if os.environ.get("STANZA_PROVIDER", None) == "web":
            logging.info("Using stanza web provider")
            createStanzaPipeline = createStanzaWebPipeline
        else:
            logging.info("Running stanza locally")
            createStanzaPipeline = createStanzaLocalPipeline

        self.parser = createStanzaPipeline()

        # Ontology engine
        onto: Any = get_ontology("owl/littlePony.owl")
        onto.load()
        graph: Any = default_world.as_rdflib_graph()
        self.ontology = o.Ontology(onto, graph)
        self.lexic = lx.Lexic(self.ontology)

    async def process(self, message: str) -> a.Answer:
        """
        Process the given message

        >>> import os, asyncio; os.environ["STANZA_PROVIDER"] = "web"

        >>> task = asyncio.get_event_loop().create_task(Questionbot().process("Who is Rainbow Dash?"))
        """
        sentenceList = await self.parser.parse(message)

        if len(sentenceList) != 1:
            return a.Answer(
                "failure", "Sorry, I can only process one sentence at a time!",
            )
        wordList = sentenceList[0]

        normal = Normal(
            lexic=self.lexic, wordList=wordList, ontology=self.ontology,
        )

        recipeList = RecipeGetter().get()
        answer = RecipeRunner(normal, recipeList).run()

        answer.info += normal.fullInfo()

        return answer


if __name__ == "__main__":
    import doctest; doctest.testmod()

