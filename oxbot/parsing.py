"""
Parse the question
"""

from .util.first import first

from typing import Any, List, Literal, TypeVar, Union
from dataclasses import dataclass
from stanza.models.common.doc import Word

from stanza.pipeline.core import Pipeline


class Failure:
    success: Literal["failure"] = "failure"


class Success:
    success: Literal["success"] = "success"


class ParseFailure_single_sentence(Failure):
    pass


ParseFailure = Union[
    ParseFailure_single_sentence,
]


@dataclass
class ParseSuccess_word_list(Success):
    wordList: List[Word]


ParseSuccess = Union[ParseSuccess_word_list]


ParseResult = TypeVar("ParseResult", ParseSuccess, ParseFailure)


@dataclass
class Parser:
    pipeline: Pipeline

    def parse(self, message: str) -> ParseResult:
        doc: Any = self.pipeline(message)

        if len(doc.sentences) != 1:
            return ParseFailure_single_sentence()

        sentence = first(doc.sentences)

        return ParseSuccess_word_list(wordList=sentence.words)

        raise Exception("")

    # def _(self): ...
