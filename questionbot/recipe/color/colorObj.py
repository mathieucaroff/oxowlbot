from ..util.formatEnumeration import formatEnumeration
from ..util.pronoun import Pronoun
from .hexColor import HexColor


class ColorObj:
    body_color: HexColor
    hair_color: HexColor
    eye_color: HexColor

    def _entry(self, name: str, color: HexColor):
        aa = "" if name.endswith('s') else 'a '
        return f"{aa}{name} {color.approxName()}"

    def tell(self, p: Pronoun, body="body", hair="hair"):
        entryList = []

        nameList = [body, hair, 'eyes']
        attrList = 'body_color hair_color eye_color'.split()
        for name, attr in zip(nameList, attrList):
            if hasattr(self, attr):
                entryList.append(self._entry(name, getattr(self, attr)))

        if len(entryList) == 0:
            return None

        text = f"{p.they} has {formatEnumeration(entryList)}."

        return text
