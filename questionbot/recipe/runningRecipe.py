from dataclasses import dataclass
from typing import Generator, Literal

from ..answer import Answer
from .. import context as c
from ..recipe.reaction import Reaction
from ..recipe.recipe import Recipe
from ..recipe.rule.rule import Rule


@dataclass
class RunningRecipe:
    answer: Answer
    context: 'c.Context'
    generator: Generator
    reaction: Reaction
    rule: Rule
    mode: Literal["rule", "reaction"] = "rule"

    def next(self):
        try:
            return self.generator.send(None)
        except StopIteration:
            if self.mode == "rule":
                self.generator = self.startReaction()
                self.mode = "reaction"
                return self.next()
            else:
                raise

    @staticmethod
    def start(recipe: Recipe, context: 'c.Context'):
        answer = Answer("ok", "")

        return RunningRecipe(
            answer=answer,
            context=context,
            generator=recipe.rule.run(context, answer),
            reaction=recipe.reaction,
            rule=recipe.rule,
        )

    def startReaction(self):
        yield "Answer"
        yield self.reaction.react(
            context=self.context,
            lemmaData=self.rule.getLemmaData(),
            answer=self.answer,
        )
        yield self.answer

        return
