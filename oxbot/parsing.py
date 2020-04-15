"""
Parse the question
"""

from dataclasses import dataclass
from typing import Any, List, Literal, TypeVar, Union

from stanza.models.common.doc import Word
from stanza.pipeline.core import Pipeline

from .util.cached_property import cached_property
from .util.first import first


class ParsingFailure:
    success: Literal["failure"] = "failure"


class ParsingSuccess:
    success: Literal["success"] = "success"


class ParseFailure_single_sentence(ParsingFailure):
    pass


ParseFailure = Union[
    ParseFailure_single_sentence,
]


@dataclass
class ParseSuccess_word_list(ParsingSuccess):
    wordList: List[Word]

    @cached_property
    def normalSentence(self) -> str:
        normalWordList = []
        for word in self.wordList:
            normalWordList.append(self._normalWord(word))
        return " ".join(normalWordList)

    def _normalWord(self, word: Word) -> str:
        return f""


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
