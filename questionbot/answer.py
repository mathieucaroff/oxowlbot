from dataclasses import dataclass
from oxbot.datatype.pword import PWord
from typing import List


"""
Produce the answer using the parse result and the ontology query result
"""


@dataclass
class Answer:
    text: str
    info: str = ""


class AnswerEngine:
    def process(self, parse_result: List[List[PWord]]) -> Answer:
        t = type(parse_result)
        if len(parse_result) != 1:
            return Answer("Sorry, I can only process one sentence at a time!")
        return self._word_list(sentence=parse_result[0])

    def _word_list(self, sentence: List[PWord]) -> Answer:
        info = "\n".join(w.pretty_print() for w in parser_result)
        normal = normalSentence(sentence)
        info += "\n" + normal
        return Answer(normal + "\n", info)
