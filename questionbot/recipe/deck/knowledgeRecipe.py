from functools import lru_cache
from .. import reaction as rt
from .. import recipe as rc
from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru


template = """
n {name}
c {classBlock}
lrb {lRelationBlock}
rrb {rRelationBlock}
"""


def formatList(li):
    return "\n".join(f"- {entry}" for entry in li)


class KnowledgeReaction(rt.Reaction):
    def react(self, context: Context, lemmaData: LemmaData, answer: a.Answer):
        individualName = lemmaData[0]
        info = context.ontology.individualInfoQuery(individualName)

        classBlock = formatList(info.classList)
        lRelationBlock = formatList(info.leftRelationList)
        rRelationBlock = formatList(info.rightRelationList)

        answer.text += template.format(
            name=individualName,
            classBlock=classBlock,
            lRelationBlock=lRelationBlock,
            rRelationBlock=rRelationBlock,
        )


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

