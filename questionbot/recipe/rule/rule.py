"""
Rule is defined by a list of LexicalFragments
"""

from dataclasses import dataclass, field
from functools import cached_property
from typing import Any, Generator, List, Union, cast

from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from ...recipe.lemmaData import LemmaData
from ...util.neverError import NeverError
from .fragment import ConstantFragment
from .sentencePattern import SentencePattern


@dataclass
class Rule:
    name: str
    shape: str
    fragmentList: List[Union[lxf.LexicalFragment, ConstantFragment]]
    _lemmaData: LemmaData = field(default_factory=LemmaData)

    @cached_property
    def lexicalFragmentList(self):
        return [
            f for f in self.fragmentList if isinstance(f, lxf.LexicalFragment)
        ]

    def run(self, context: Context, answer: a.Answer) -> Generator:
        wordList = context.wordList
        normalSentence = context.sentence

        yield "Syntax Analysis"

        sentencePattern = SentencePattern(
            fragmentList=cast(Any, self.fragmentList)
        )

        result = sentencePattern.extractEachActiveFragment(normalSentence)
        if result is not None:
            activeExtractList = result
        else:
            yield False
            raise NeverError()
        yield True

        yield "Lexical Analysis"
        assert len(activeExtractList) == len(self.lexicalFragmentList)

        activeExtract = ["<I actually can't tell which word it is>"]
        try:
            for wordIdStrList, fragment in zip(
                activeExtractList, self.lexicalFragmentList
            ):
                activeExtract = [
                    wordList[int(idStr) - 1].text for idStr in wordIdStrList
                ]

                lexicalChunk = fragment.obtainLexicalChunk(
                    activeExtract=activeExtract, lexic=context.lexic, answer=answer
                )

                self._lemmaData.append(lexicalChunk)
        except KeyError:
            yield False
            yield " ".join(activeExtract)
        yield True

    def getLemmaData(self):
        assert len(self._lemmaData) == len(self.lexicalFragmentList)

        return self._lemmaData
