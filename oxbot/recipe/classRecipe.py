from typing import Any, List

from .baseRecipe import BaseRecipe
from .pattern import Pattern


class ClassRecipe(BaseRecipe):
    def __init__(self):
        BaseRecipe.__init__(self, [Pattern(r".*be.*")])

    def query(self) -> str:
        assert self.didMatch
        return ""

    def describe(self) -> str:
        return ""
