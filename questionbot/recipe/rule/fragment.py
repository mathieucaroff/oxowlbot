from dataclasses import dataclass
import re

from ...recipe.rule.pattern import Pattern


@dataclass
class BaseFragment:
    overview: str

@dataclass
class ConstantFragment(BaseFragment):
    pass

class ActiveFragment(BaseFragment):
    detail: str

    def __init__(self, overview, detail):
        self.overview = overview.format(detail=detail.replace('!', ''))
        self.detail = detail

    def extract(self, target_part: str):
        """
        Return the list of the first group in each match of the .detail regex
        """
        return [m.group(1) for m in re.finditer(Pattern(self.detail).pat, target_part)]