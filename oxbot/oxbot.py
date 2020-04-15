from typing import Any
import stanza

from .redirect import redirect_stderr

with redirect_stderr():
    from owlready2 import get_ontology, default_world

# pyright: strict

# /!\ REMEMBER TO COPY owl/littlePony.owl again


class Oxbot:
    graph: Any

    def __init__(self):
        get_ontology("owl/littlePony.owl").load()
        self.graph = default_world.as_rdflib_graph()
        with redirect_stderr():
            self.nlp = stanza.Pipeline("en")

    async def process(self, message: str):
        doc: Any = self.nlp(message)

        if len(doc.sentences) != 1:
            return "Sorry, I can only process one sentence at a time!"

        sentence = next(doc.sentences)
        answer = ""

        for word in sentence.words:
            answer += f"{word.lemma}\n"

        return f"-{message}-"
