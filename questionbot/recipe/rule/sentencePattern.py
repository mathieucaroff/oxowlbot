from dataclasses import dataclass
from typing import List, Union

from ...util.cached_property import cached_property
from .fragment import ActiveFragment, BaseFragment
from .pattern import Pattern


@dataclass
class SentencePattern:
    fragmentList: List[BaseFragment]

    @cached_property
    def concatenatedPattern(self):
        return Pattern(
            "".join(fragment.overview for fragment in self.fragmentList)
        )

    def match(self, target: str):
        return self.concatenatedPattern.match(target)

    def extract(self, target: str) -> Union[List[List[str]], None]:
        """
        Extract the all the matches of each fragment
        """
        m = self.match(target)
        if m is None:
            return None
        activeFragmentList = [f for f in self.fragmentList if isinstance(f, ActiveFragment)]

        assert len(m.groups()) == len(activeFragmentList)

        result: List[List[str]] = []
        for text, fragment in zip(m.groups(), activeFragmentList):
            groupList = fragment.extract(text)
            assert len(groupList) > 0
            result.append(groupList)

        return result
