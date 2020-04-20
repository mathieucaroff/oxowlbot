from dataclasses import dataclass
import re


@dataclass
class BaseFragment:
    overview: str

@dataclass
class ConstantFragment(BaseFragment):
    pass

@dataclass
class ActiveFragment(BaseFragment):
    detail: str

    def extract(self, target_part: str):
        """
        Return the list of the first group in each match of the .detail regex
        """
        if self.detail is None: raise ValueError()
        return [m.group(1) for m in re.finditer(self.detail, target_part)]