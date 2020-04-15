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


class Answer:
    def obtain(self, parse_result: ParseResult) -> str:
        t = type(parse_result)
        try:
            method = recipe[t]
            return method(self, parse_result)
        except KeyError:
            return f"INTERNAL ERROR missing implementation for `{t}`"

    def _word_list(self, parser_result: ParseSuccess_word_list) -> str:
        text = ""
        for word in parser_result.wordList:
            text += f"{word.lemma}\n"
        return text


"""
Recipes map a parse result to an ontology action and an answer strategy
"""
recipe = {
    ParseFailure_single_sentence: just_text(
        "Sorry, I can only process one sentence at a time!"
    ),
    ParseSuccess_word_list: Answer._word_list,
}
