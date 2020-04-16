from dataclasses import dataclass
from typing import Pattern
import re


@dataclass
class Pattern:
    pat: str

    def match(self, target):
        result = re.search(self.pat, target)
        if result is None:
            return None
        else:
            return result
