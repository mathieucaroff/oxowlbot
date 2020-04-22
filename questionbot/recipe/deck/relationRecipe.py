from .. import reaction as rt
from .. import recipe as rc
from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru
from ..util.digitToWord import digitToWord
from ..util.formatEnumeration import formatEnumeration
from ..util.formatListing import formatListing


class RelationReaction(rt.Reaction):
    def react(self, context: Context, lemmaData: LemmaData, answer: a.Answer):
        relationList, individualName = lemmaData

        individualList = context.ontology.relationIndividualQuery(
            individualName=individualName, relationList=relationList, mode="inward"
        )

        rText = " ".join(relationList).replace('_', ' ')
        descriptin = f"{rText} {individualName}"

        count = len(individualList)
        countWord = digitToWord(count)

        if count == 0:
            answer.text += f"There are no {descriptin}.\n"
        elif count == 1:
            answer.text += f"There's only one {descriptin}.\n"
        elif count <= 10:
            answer.text += f"There are {countWord} {descriptin}: {formatEnumeration(individualList)}.\n"
        else:
            answer.text += f"There are {countWord} {descriptin}. They are {formatListing(individualList)}"


class RelationRecipeGroup:
    def createRecipeList(self):
        relationReaction = RelationReaction()

        return [
            rc.Recipe(
                relationReaction,
                ru.Rule(
                    name="Relation A",
                    shape="Who is <relation> of <I>?",
                    fragmentList=[
                        deck.whoIs,
                        lxf.LexicalFragment(
                            kind="relation", fragment=deck.relation,
                        ),
                        lxf.LexicalFragment(
                            kind="individual", fragment=deck.nominal,
                        ),
                    ],
                ),
            ),
        ]
