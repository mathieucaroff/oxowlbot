from typing import Any
from ..util.formatEnumeration import formatEnumeration
from ..util.pronoun import Pronoun
from .hexColor import HexColor


class ColorObj:
    body_color: HexColor
    hair_color: HexColor
    eye_color: HexColor

    def _entry(self, aaa: Any, name: str, color: HexColor):
        a_ = "" if name.endswith('s') else next(aaa)
        return f"{a_}{color.approxName()} {name}"

    def tell(self, p: Pronoun, body="body", hair="hair"):
        entryList = []

        nameList = [body, hair, 'eyes']
        attrList = 'body_color hair_color eye_color'.split()
        aaa = iter(['a ', '', ''])
        for name, attr in zip(nameList, attrList):
            if hasattr(self, attr):
                entryList.append(self._entry(aaa, name, getattr(self, attr)))

        if len(entryList) == 0:
            return None

        text = f"{p.They_have} {formatEnumeration(entryList)}. "

        return text
