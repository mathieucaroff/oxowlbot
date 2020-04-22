import re

class Preprocessor:
    def process(self, text):
        re.split(r"\b *| *\b", text)
