import logging
from typing import Tuple


class HexColor(str):
    rgb: Tuple[int, int, int]

    vividColorDict = {}
    tintlessColorDict = {}

    def __new__(cls, *a, **kw):
        self = str.__new__(cls, *a, **kw)
        number = int(self, 16)
        self.r = number & 0xFF0000 >> 16
        self.g = number & 0x00FF00 >> 8
        self.b = number & 0x0000FF
        self.rgb = (self.r, self.g, self.b)
        return self

    def distanceTo(self, other: "HexColor"):
        return sum(a * b for a, b in zip(self.rgb, other.rgb))

    def approxName(self):
        colorWithWeightedDistances = [
            (self.distanceTo(color) * factor, name)
            for dictName, factor in [
                ("vividColorDict", 1),
                ("tintlessColorDict", 3),
            ]
            for name, color in getattr(HexColor, dictName).items()
        ]
        _dist, colorName = min(colorWithWeightedDistances)
        return colorName


HexColor.vividColorDict = dict(
    red=HexColor("FF0000"),
    green=HexColor("00FF00"),
    blue=HexColor("0000FF"),
    light_blue=HexColor("00FFFF"),
    pink=HexColor("FF00FF"),
    yellow=HexColor("FFFF00"),
    purple=HexColor("4C00ff"),
    orange=HexColor("FF8000"),
    brown=HexColor("7C4F2B"),
)


HexColor.tintlessColorDict = dict(
    grey=HexColor("808080"),
    black=HexColor("000000"),
    white=HexColor("FFFFFF"),
    dark_grey=HexColor("404040"),
    light_grey=HexColor("C0C0C0"),
)
