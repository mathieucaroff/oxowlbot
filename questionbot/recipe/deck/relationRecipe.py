from questionbot.recipe.util.capitalize import capitalize
from .. import reaction as rt
from .. import recipe as rc
from ... import answer as a
from ... import lexicalFragment as lxf
from ... import context as c
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru
from ..util.digitToWord import digitToWord
from ..util.formatEnumeration import formatEnumeration
from ..util.formatListing import formatListing


class RelationReaction(rt.Reaction):
    async def react(self, context: 'c.Context', lemmaData: LemmaData, answer: a.Answer):
        relationList, individualName = lemmaData

        individualList = context.ontology.relationIndividualQuery(
            individualName=individualName, relationList=relationList, mode="inward"
        )

        rText = " ".join(relationList)
        description = f"{rText} {individualName}"

        count = len(individualList)
        countWord = digitToWord(count)
        CountWord = capitalize(countWord)

        if count == 0:
            text = f"No creature is {description}.\n"
        elif count == 1:
            text = f"Only one creature is {description}.\n"
        elif count <= 10:
            text = f"{CountWord} creatures are {description}: {formatEnumeration(individualList)}.\n"
        else:
            text = f"{CountWord} creatures are {description}. They are:\n{formatListing(individualList)}\n"

        answer.text += text.replace('_', ' ')


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
