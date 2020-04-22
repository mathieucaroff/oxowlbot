from .. import reaction as rt
from .. import recipe as rc
from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import sentencePattern as sp
from ..rule import rule as ru


class RelationReaction(rt.Reaction):
    def react(
        self, context: Context, lemmaData: LemmaData, answer: a.Answer
    ):
        raise NotImplemented()


class RelationRecipeGroup:
    def createRecipeList(self):
        knowledgeReaction = RelationReaction()

        return [
            rc.Recipe(
                knowledgeReaction,
                ru.Rule(
                    name="Relation A",
                    shape="Who is <relation> of <I>?",
                    fragmentList=[
                        deck.whoIs,
                        lxf.LexicalFragment(
                            kind="relation", fragment=deck.relation,
                        ),
                        lxf.LexicalFragment(
                            kind='individual', fragment=deck.nominal,
                        )
                    ],
                ),
            ),
        ]
