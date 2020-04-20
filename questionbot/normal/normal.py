from typing import List

from .normalSentence import normalSentence

from .. import lexic as lx
from .. import ontology as o
from ..stanza.pword import PWord


class Normal:
    """
    Normal is box Class to combine the sentenced being processed with all the tools from the Questionbot class needed to process it.
    """

    ontology: "o.Ontology"
    lexic: "lx.Lexic"
    wordList: List["PWord"]
    sentence: str

    def __init__(
        self, ontology: "o.Ontology", lexic: "lx.Lexic", wordList: List["PWord"]
    ):
        self.ontology = ontology
        self.lexic = lexic
        self.wordList = wordList
        self.sentence = normalSentence(wordList)

    def fullInfo(self):
        return "\n".join(w.pretty_print() for w in self.wordList)
