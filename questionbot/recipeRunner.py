from dataclasses import dataclass
from questionbot.recipe.runningRecipe import RunningRecipe

from typing import List

from . import answer as a
from .normal.normal import Normal
from .util.eprint import eprint
from .recipe import recipe as rc

EXCLUSION_MESSAGE = "Recipe {name} is non-conform, yielding {output} when {target} was expected. It was excluded."


@dataclass
class RecipeRunner:
    normal: Normal
    recipeList: List[rc.Recipe]

    def run(self) -> a.Answer:
        finalText: str = ""

        runningRecipeList = [
            recipe.start(normal=self.normal) for recipe in self.recipeList
        ]

        #
        SA = "Syntax Analysis"
        #
        runRecipeList(
            recipeList=runningRecipeList,
            targetOutput=SA,
            message=EXCLUSION_MESSAGE,
        )

        runRecipeList(runningRecipeList, targetOutput=True)

        validSyntaxList = runningRecipeList[:]

        if len(validSyntaxList) == 0:
            text = (
                "I tried to understand your sentence using {} different patterns, but I couldn't do it. "
                'Say "Help" if you want me to give you some examples of sentences I understand.'
            ).format(len(self.recipeList))

            return a.Answer("failure", text)

        #
        LA = "Lexical Analysis"
        #
        runRecipeList(runningRecipeList, LA, EXCLUSION_MESSAGE)

        runRecipeList(runningRecipeList, targetOutput=True)

        validLexicList = runningRecipeList[:]

        if len(validLexicList) == 0:
            text = (
                "Your sentence matches {count} of the patterns I know:\n"
                "- {patternShapeList}\n"
                'but the work you chose "{word}" is unknown to me in these contexts.'
            ).format(
                count=len(validSyntaxList),
                patternShapeList="\n- ".join(
                    recipe.origin.rule.shape for recipe in validSyntaxList
                ),
                word=validSyntaxList[0].next(),
            )

            return a.Answer("failure", text)

        #
        # Form ambiguity
        #
        chosenRecipe = validLexicList[0]

        if len(validLexicList) > 1:
            text = (
                "Your sentence completly matches {count} of the forms:\n"
                "- {formShapeList}\n"
                'I selected the first of them "{}" and worked from there\n\n'
            ).format(
                count=len(validLexicList),
                formShapeList="\n- ".join(recipe.origin.rule.shape for recipe in validLexicList),
                word=validLexicList[0].origin.rule.shape,
            )

            chosenRecipe.answer.warning += text

        #
        AN = "Answer"
        #
        assert chosenRecipe.next() == AN, f"Buggy Recipy '{AN}'"

        return chosenRecipe.next()


# - [word A]
# - [word B]
# I selected the first of them "[word A]" and worked from there."""


def runRecipeList(recipeList: List[RunningRecipe], targetOutput, message: str = None):
    """
    Calls .next() on each generator of the list, and expect each of them to return {targetOutput}. The ones that do not are removed from the generator list. If a {message} is provided, it'll be printed on stderr for each generator removed.

    the {message} variable can use the following python format template values:
    - name - The name of the recipe
    - output - The value outputed by the generator
    - target - The value of "targetOutput"
    """
    for recipe in recipeList:
        output = recipe.next()
        if output != targetOutput:
            recipeList.remove(recipe)
        elif message is not None:
            eprint(
                message.format(
                    name=recipe.__qualname__,
                    output=output,
                    target=targetOutput,
                )
            )
