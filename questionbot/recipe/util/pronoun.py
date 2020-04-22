from dataclasses import dataclass
from functools import cached_property
from ..util.capitalize import capitalize


@dataclass
class Pronoun:
    they: str
    their: str
    be: str
    have: str

    @cached_property
    def They(self):
        return capitalize(self.they)

    @cached_property
    def they_be(self):
        return f"{self.they} {self.be}"

    @cached_property
    def They_be(self):
        return f"{self.They} {self.be}"

    @cached_property
    def they_have(self):
        return f"{self.they} {self.have}"

    @cached_property
    def They_have(self):
        return f"{self.They} {self.have}"

    @cached_property
    def Their(self):
        return capitalize(self.their)
