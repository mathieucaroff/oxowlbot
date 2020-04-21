from .. import reaction as rt
from .. import recipe as rc
from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru


template = """
{}
"""


class KnowledgeReaction(rt.Reaction):
    def react(self, context: Context, lemmaData: LemmaData, answer: a.Answer):
        individualName = lemmaData[0]
        allInfo = context.ontology.allIndividualInfoQuery(individualName)

        answer.text += template.format(**allInfo.asdict())


class KnowledgeRecipeGroup:
    def createRecipeList(self):
        knowledgeReaction = KnowledgeReaction()

        return [
            rc.Recipe(knowledgeReaction, ru.Rule(
                name="Knowledge A",
                shape="Who is <I>?",
                fragmentList=[
                    deck.whoIs,
                    lxf.LexicalFragment(
                        kind="individual",
                        fragment=deck.nominal
                    ),
                ],
            )),
        ]

