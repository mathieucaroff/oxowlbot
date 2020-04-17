from dataclasses import dataclass

from oxbot.parsing import (
    ParseResult,
    ParseFailure_single_sentence,
    ParseSuccess_word_list,
)

"""
Produce the answer using the parse result and the ontology query result
"""


def just_text(text: str):
    def constantClosure(_self, _parse_result) -> str:
        return text

    return constantClosure


@dataclass
class Answer:
    text: str
    info: str = ""


class AnswerEngine:
    def process(self, parse_result: ParseResult) -> Answer:
        t = type(parse_result)
        try:
            method = recipe[t]
            return method(self, parse_result)
        except KeyError:
            return Answer(f"INTERNAL ERROR missing implementation for `{t}`")

    def _word_list(self, parser_result: ParseSuccess_word_list) -> Answer:
        info = "\n".join(w.pretty_print() for w in parser_result.wordList)
        info += "\n" + parser_result.normalSentence
        return Answer(parser_result.normalSentence + "\n", info)


"""
Recipes map a parse result to an ontology action and an answer strategy
"""
recipe = {
    ParseFailure_single_sentence: just_text(
        "Sorry, I can only process one sentence at a time!"
    ),
    ParseSuccess_word_list: AnswerEngine._word_list,
}
