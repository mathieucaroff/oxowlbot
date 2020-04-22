from dataclasses import dataclass
from typing import List

from . import lexic as lx
from . import ontology as o
from .matchableSentence import matchableSentence
from .stanza.pword import PWord


@dataclass
class Context:
    """
    Context is a box class to combine the sentenced being processed with all the tools from the Questionbot class needed to process it.
    """

    lexic: "lx.Lexic"
    ontology: "o.Ontology"
    sentence: str
    wordList: List["PWord"]

    def stanzaInfo(self):
        return "\n".join(w.pretty_print() for w in self.wordList)
