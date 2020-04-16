"""
Parse the question
"""

from dataclasses import dataclass
from typing import Awaitable, Callable, List, Literal, TypeVar, Union

from oxbot.datatype.pword import PWord

from .util.cached_property import cached_property


symbolMap = {
    -6: "<=-",
    -5: "<-=",
    -4: "<--",
    -3: "<=",
    -2: "<-",
    -1: "<",
    0: "==",
    1: ">",
    2: "->",
    3: "=>",
    4: "-->",
    5: "=->",
    6: "-=>",
}


class ParsingFailure:
    success: Literal["failure"] = "failure"


class ParsingSuccess:
    success: Literal["success"] = "success"


class ParseFailure_single_sentence(ParsingFailure):
    pass


ParseFailure = Union[ParseFailure_single_sentence]


@dataclass
class ParseSuccess_word_list(ParsingSuccess):
    wordList: List[PWord]

    @cached_property
    def normalSentence(self) -> str:
        normalWordList = []
        for word in self.wordList:
            normalWordList.append(self._normalWord(word))
        return " ".join(normalWordList)

    def _normalWord(self, word: PWord) -> str:
        diff = word.head - int(word.id)
        if word.head == 0:
            diff = 0
        symbol = symbolMap.get(diff)
        number = "x"
        for piece in word.feats.split("|"):
            partList = piece.split("=")
            if len(partList) != 2:
                continue
            left, right = partList
            if left == "Number":
                if right == "Plur":
                    number = "2"
                if right == "Sing":
                    number = "1"

        w = word
        return f":{w.id}_L{w.lemma}_u{w.upos}_N{number}_R{w.deprel}_{symbol}."


ParseSuccess = Union[ParseSuccess_word_list]


ParseResult = TypeVar("ParseResult", ParseSuccess, ParseFailure)


@dataclass
class Parser:
    stanzaPipeline: Callable[[str], Awaitable[List[List[PWord]]]]

    async def parse(self, message: str) -> ParseResult:
        sentenceList = await self.stanzaPipeline(message)

        if len(sentenceList) != 1:
            return ParseFailure_single_sentence()

        sentence = sentenceList[0]

        return ParseSuccess_word_list(wordList=sentence)
