from dataclasses import dataclass
from typing import List

from questionbot import recipe

from . import answer as a
from .context import Context
from .recipe import recipe as rc
from .recipe import runningRecipe as rr
from .util.eprint import eprint


EXCLUSION_MESSAGE = "Recipe {name} is non-conform, yielding {recipeOutput} when {targetOutput} was expected. It was excluded."


@dataclass
class RecipeRunner:
    """
    Allow to run a list of runningRecipes in the context of a context.
    """

    context: Context
    recipeList: List[rc.Recipe]

    def run(self) -> a.Answer:
        runningRecipeList = [
            rr.RunningRecipe.start(recipe=recipe, context=self.context)
            for recipe in self.recipeList
        ]

        #
        SA = "Syntax Analysis"
        #
        # ECA - Syntax Failure
        #
        runRecipeList(runningRecipeList, SA, EXCLUSION_MESSAGE)

        runRecipeList(runningRecipeList, targetOutput=True)

        validSyntaxList = runningRecipeList[:]

        if len(validSyntaxList) == 0:
            text = (
                "I tried to understand your sentence using {} different patterns, but none of them worked. "
                'Say "Help" if you want me to give you some examples of sentences I understand.\n'
            ).format(len(self.recipeList))

            return a.Answer("failure", text)

        #
        LA = "Lexical Analysis"
        #
        # ECB - Lexical Failure
        #
        runRecipeList(runningRecipeList, LA, EXCLUSION_MESSAGE)

        runRecipeList(runningRecipeList, targetOutput=True)

        validLexicList = runningRecipeList[:]

        if len(validLexicList) == 0:
            text = (
                "Your sentence matches {count} of the patterns I know:\n"
                "- {patternShapeList}\n"
                'but the word you chose "{word}" is unknown to me in these contexts.\n'
            ).format(
                count=len(validSyntaxList),
                patternShapeList="\n- ".join(
                    recipe.rule.shape for recipe in validSyntaxList
                ),
                word=validSyntaxList[0].next(),
            )

            return a.Answer("failure", text)

        #
        # ECC - Form ambiguity
        #
        chosenRecipe = validLexicList[0]

        if len(validLexicList) > 1:
            text = (
                "Your sentence completly matches {count} of the forms:\n"
                "- {formShapeList}\n"
                'I selected the first of them "{select}" and worked from there\n\n'
            ).format(
                count=len(validLexicList),
                formShapeList="\n- ".join(
                    recipe.rule.shape for recipe in validLexicList
                ),
                select=validLexicList[0].rule.shape,
            )

            chosenRecipe.answer.warning += text

        #
        AN = "Answer"
        #
        out = chosenRecipe.next()
        assert out == AN, f"Buggy Recipy '{AN=} {out=}'"

        answer = chosenRecipe.next()
        assert isinstance(answer, a.Answer), f"answer is {answer}"
        return answer


def runRecipeList(
    recipeList: List["rr.RunningRecipe"], targetOutput, message: str = None
):
    """
    Calls .next() on each generator of the list, and expect each of them to return {targetOutput}. The ones that do not are removed from the generator list. If a {message} is provided, it'll be printed on stderr for each generator removed.

    the {message} variable can use the following python format template values:
    - name - The name of the recipe
    - output - The value outputed by the generator
    - target - The value of "targetOutput"
    """
    for recipe in [*recipeList]:
        recipeOutput = recipe.next()

        if recipeOutput != targetOutput:
            recipeList.remove(recipe)
            if message is not None:
                eprint(
                    message.format(
                        name=recipe.rule.name,
                        recipeOutput=recipeOutput,
                        targetOutput=targetOutput,
                    )
                )
    print("RRL", targetOutput, "DONE", len(recipeList))
