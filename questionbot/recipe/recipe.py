from dataclasses import dataclass

from .. import answer as a

from ..normal.normal import Normal
from ..recipe.runningRecipe import RunningRecipe
from .reaction import Reaction
from .rule import rule as r


@dataclass
class Recipe:
    rule: r.Rule
    reaction: Reaction

    def start(self, normal: Normal):
        answer = a.Answer("ok", "")

        return RunningRecipe(
            origin=self,
            generator=self._run(normal, answer=answer),
            answer=answer,
        )

    def _run(self, normal: Normal, answer: a.Answer):
        runningRule = self.rule.run(normal)

        yield from [x for x, _ in zip(runningRule, range(5))]

        rule_result = runningRule.send(None)

        return self.reaction.react(
            normal=normal, lemmaData=rule_result, answer=answer,
        )
