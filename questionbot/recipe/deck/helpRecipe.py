from ... import answer as a
from ...context import Context
from .. import reaction as rt
from .. import recipe as rc
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru


HELP_MESSAGE = """
Here are some questions I can answer:

"Who is Pinkie Pie?"
"Who is child of Pear Butter?"
"Who is an alicorn?"
"Who is friend with Twilight Sparkle?"
"Who is a child of a child of Twilight Velvelt?"
""".lstrip()


class HelpReaction(rt.Reaction):
    def react(self, context: Context, lemmaData: LemmaData, answer: a.Answer):
        answer.text += HELP_MESSAGE


class HelpRecipeGroup:
    def createRecipeList(self):
        helpReaction = HelpReaction()

        return [
            rc.Recipe(
                helpReaction,
                ru.Rule(
                    name="Help A",
                    shape="Help!",
                    fragmentList=[deck.help],
                ),
            ),
        ]
