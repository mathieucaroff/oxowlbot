import logging
from typing import Any

from . import answer as a
from . import lexic as lx
from . import ontology as o
from .context import Context
from .matchableSentence import matchableSentence
from .recipe.recipeGetter import RecipeGetter
from .recipeRunner import RecipeRunner
from .stanza.stanzaProvider import StanzaPipeline, createStanzaPipeline
from .util.redirect import redirect_stderr

with redirect_stderr():
    from owlready2 import get_ontology
    from owlready2.reasoning import sync_reasoner


class Questionbot:
    parser: StanzaPipeline
    ontology: o.Ontology
    lexic: lx.Lexic

    def __init__(self):
        # Parser engine, stanza
        self.parser = createStanzaPipeline()

        # Ontology engine
        onto: Any = get_ontology("owl/littlePony.owl").load()
        if onto.Rarity is None:
            logging.warn(
                f"RARITY CHECK FAILED"
            )

        with onto:
            with redirect_stderr():
                sync_reasoner()

        self.ontology = o.Ontology(onto)

        # Ontology lexic checker
        self.lexic = lx.Lexic(self.ontology)

    async def process(self, message: str) -> a.Answer:
        """
        Process the given message

        >>> from asyncio import run
        >>> run(Questionbot().process("Who is a kirin?"))

        # >>> run(Questionbot().process("Who is Rainbow Dash?"))
        # >>> run(Questionbot().process("Who is a cat?"))
        # >>> run(Questionbot().process("Who is friend with Twilight Sparkle?"))
        """
        sentenceList = await self.parser.parse(message)

        if len(sentenceList) != 1:
            return a.Answer(
                "failure", "Sorry, I can only process one sentence at a time!",
            )
        wordList = sentenceList[0]

        context = Context(
            lexic=self.lexic,
            ontology=self.ontology,
            sentence=matchableSentence(wordList),
            wordList=wordList,
        )

        recipeList = RecipeGetter().get()
        answer = RecipeRunner(context, recipeList).run()

        answer.info += context.sentence + "\n"
        answer.info += context.fullInfo()

        return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
