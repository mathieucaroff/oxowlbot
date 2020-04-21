from dataclasses import dataclass

from .reaction import Reaction
from .rule import rule as ru


@dataclass
class Recipe:
    reaction: Reaction
    rule: ru.Rule

