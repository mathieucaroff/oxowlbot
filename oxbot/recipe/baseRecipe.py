from dataclasses import dataclass
from typing import Any, List

from oxbot.recipe.pattern import Pattern


@dataclass
class BaseRecipe:
    patternList: List[Pattern]
    didMatch: bool = False
    matchResult: Any = 0

    def match(self, normalSentence) -> bool:
        for pattern in self.patternList:
            m = pattern.match(normalSentence)
            if m is not None:
                self.didMatch = True
                self.matchResult = m
                break
        return self.didMatch
