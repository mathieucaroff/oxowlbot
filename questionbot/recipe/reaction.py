import abc

from .. import answer as a
from .. import context as c
from .lemmaData import LemmaData


class Reaction:
    @abc.abstractmethod
    async def react(
        self, context: 'c.Context', lemmaData: LemmaData, answer: a.Answer
    ) -> None:
        ...
