"""
Rule is defined by a list of LexicalFragments
"""

from dataclasses import dataclass
from typing import Any, Generator, List, Union, cast

from ... import answer as a
from ... import lexic as lx
from ... import lexicalFragment as lxf
from ...normal.normal import Normal
from ...util.cached_property import cached_property
from ...util.neverError import NeverError
from .fragment import ConstantFragment
from .sentencePattern import SentencePattern


@dataclass
class Rule:
    name: str
    shape: str
    fragmentList: List[Union[lxf.LexicalFragment, ConstantFragment]]

    @cached_property
    def lexicalFragmentList(self):
        return [
            f for f in self.fragmentList if isinstance(f, lxf.LexicalFragment)
        ]

    def run(self, normal: Normal,) -> Generator:
        wordList = normal.wordList
        normalSentence = normal.sentence

        yield "Syntax Analysis"

        sentencePattern = SentencePattern(
            fragmentList=cast(Any, self.fragmentList)
        )

        extractOrNone = sentencePattern.extract(normalSentence)
        if extractOrNone is not None:
            extract = extractOrNone
        else:
            yield False
            raise NeverError()
        yield True

        # yield "Shape"

        yield "Lexical Analysis"
        assert len(extract) == len(self.lexicalFragmentList)

        for wordIdStrList, fragment in zip(extract, self.lexicalFragmentList):
            extract = [wordList[int(idStr) - 1].text for idStr in wordIdStrList]

            lexicalAnswer = a.Answer("ok", "")

            fragment.obtainLexicalTerm(
                extract=extract, lexic=normal.lexic, answer=lexicalAnswer
            )
