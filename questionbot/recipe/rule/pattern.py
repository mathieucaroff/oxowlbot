import re


class Pattern:
    pat: str

    def __init__(self, pat):
        self.pat = (
            (pat)
            .replace("~", r" +(?::.*?\. +)??")
            .replace("__", r":[^\.]*\.")
            .replace("<!!", r":(\d+),")
            .replace("<", r":[^\.]*?")
            .replace(",", r"_[^\.]*?")
            .replace(">", r"_[^\.]*\.")
        )

    def match(self, target: str):
        return re.search(self.pat, target.strip())

    # def extract(self, target: str):
    #     return re.sub(self.pat, '$1', target.strip())
