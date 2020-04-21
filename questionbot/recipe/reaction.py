import abc

from .. import answer as a
from ..context import Context
from .lemmaData import LemmaData


class Reaction:
    @abc.abstractmethod
    def react(
        self, context: Context, lemmaData: LemmaData, answer: a.Answer
    ) -> None:
        ...
