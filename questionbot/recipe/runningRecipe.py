from dataclasses import dataclass
from ..answer import Answer
from typing import Generator
from questionbot.recipe import recipe as rc


@dataclass
class RunningRecipe:
    origin: 'rc.Recipe'
    generator: Generator
    answer: Answer

    def next(self):
        return self.generator.send(None)
