import abc

from .. import answer as a
from ..normal.normal import Normal
from .lemmaData import LemmaData

class Reaction:
    @abc.abstractmethod
    def react(self, normal: Normal, lemmaData: LemmaData, answer: a.Answer) -> None: ...
