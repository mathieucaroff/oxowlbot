from dataclasses import dataclass
from typing import Pattern
import re


class Pattern:
    pat: str

    def __init__(self, pat):
        self.pat = (
            (pat)
            .replace("~", r" +:.*?\. +")
            .replace("__", r":[^\.]*\. ")
            .replace("<!!", r":(\d+),")
            .replace("<", r":[^\.]*?")
            .replace(",", r"_[^\.]*?")
            .replace(">", r"_[^\.]*\.")
        )

    def match(self, target):
        result = re.search(self.pat, target.trim())
        if result is None:
            return None
        else:
            return result
