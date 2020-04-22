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


class HelpReaction(rt.Reaction):
    async def react(
        self, context: "c.Context", lemmaData: LemmaData, answer: a.Answer
    ):
        text = "Here are some questions I can answer:\n\n"

        questionList = []

        for questionTemplate in questionTemplateList:
            question = questionTemplate
            if "{C}" in question:
                className = random.choice([*context.lexic.classTable.values()])
                question = question.format(C=className)
            if "{I}" in question:
                name = random.choice([*context.lexic.individualTable.values()])
                question = question.format(I=name)

            try:
                answer = await context.questionbot.process(question)
            except Exception:
                answer = a.Answer("failure", "")

            if answer.status == "ok":
                questionList.append(question)

        answer.text += text + "\n".join(questionList) + "\n"



class HelpRecipeGroup:
    def createRecipeList(self):
        helpReaction = HelpReaction()

        return [
            rc.Recipe(
                helpReaction,
                ru.Rule(
                    name="Help A", shape="Help!", fragmentList=[deck.help],
                ),
            ),
        ]
