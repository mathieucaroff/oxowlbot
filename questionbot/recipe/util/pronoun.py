from dataclasses import dataclass
from functools import cached_property


@dataclass
class Pronoun:
    they: str
    their: str
    be: str

    @cached_property
    def they_be(self):
        return f"{self.they} {self.be}"

    @cached_property
    def They_be(self):
        return self.they_be[:1].upper() + self.they_be[1:]

    @cached_property
    def Their(self):
        return self.their[:1].upper() + self.their[1:]
