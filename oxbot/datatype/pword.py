from dataclasses import dataclass

from stanza.models.common.doc import Word


@dataclass
class PWord(Word):
    id: int
    text: str
    lemma: str
    upos: str
    xpos: str
    feats: str
    head: int
    deprel: str
    misc: str

    def pretty_print(self):
        features = "id text lemma upos xpos feats head deprel".split()
        feature_str = " ".join(
            "{}={}".format(k, getattr(self, k))
            for k in features
            if getattr(self, k) is not None
        )
        return f"<{feature_str}>"
