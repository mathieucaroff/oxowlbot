import random
from ... import answer as a
from ... import context as c
from .. import reaction as rt
from .. import recipe as rc
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru


questionTemplateList = [
    "Who is {I}?",
    "Who is a {C}?",
    "Who is child of Pear Butter?",
    "Who is friend with Spike?",
    "Who is a child of a child of Twilight Velvet?",
]


class CreatorReaction(rt.Reaction):
    async def react(
        self, context: "c.Context", lemmaData: LemmaData, answer: a.Answer
    ):
        answer.text += "I was created by Mathieu CAROFF. See https://github.com/mathieucaroff/oxowlbot\n\n"


class CreatorRecipeGroup:
    def createRecipeList(self):
        creatorReaction = CreatorReaction()

        return [
            rc.Recipe(
                creatorReaction,
                ru.Rule(
                    name="Creator A",
                    shape="Who is your creator?",
                    fragmentList=[deck.whoIs, deck.creator],
                ),
            ),
            rc.Recipe(
                creatorReaction,
                ru.Rule(
                    name="Creator B",
                    shape="Who created you?",
                    fragmentList=[deck.who, deck.create],
                ),
            ),
        ]
