import statistics
from typing import Tuple, cast

from ..util.clamp import clamp


class HexColor(str):
    """
    >>> HexColor.vividColorDict['red'].rgb
    (255, 0, 0)
    >>> HexColor.ternColorDict['red'].rgb
    (161, 72, 72)
    """

    rgb: Tuple[int, int, int]

    vividColorDict = {}
    ternColorDict = {}

    def __new__(cls, *a, **kw):
        """
        >>> HexColor("AFEBCD") == HexColor("Af_eb_c_D")
        True
        >>> HexColor("F_0_0") == HexColor("F00") == HexColor("ff0000")
        True
        """
        val = a[0] if len(a) > 0 else "000000"

        if not isinstance(val, str):
            breakpoint()
            val = "000000"

        val = val.upper().strip().replace("_", "")

        if len(val) == 3:
            val = "".join(letter * 2 for letter in val)

        if len(val) != 6:
            breakpoint()
            val = "000000"

        a = [val, *a[1:]]

        #
        self = str.__new__(cls, *a, **kw)
        #

        self.r = int(self[0:2], 16)
        self.g = int(self[2:4], 16)
        self.b = int(self[4:6], 16)

        self.rgb = (self.r, self.g, self.b)

        return self

    @staticmethod
    def fromRgb(rgb: Tuple[int, int, int]):
        """
        >>> HexColor.fromRgb([0xFF, 0xEE, 0xFF]) == HexColor("FFEEFF")
        True
        >>> HexColor.fromRgb([0xFF, 0, 0]) == HexColor("FF0000")
        True
        """
        hexText = "".join(map("{:02x}".format, map(clamp(0, 255), rgb)))
        return HexColor(hexText)

    def lightness(self) -> float:
        """
        >>> HexColor("C00").lightness() == 0x44
        True
        """
        return statistics.mean(self.rgb)

    def desaturate(self, t=0.7):
        """
        Make color closer to grey. If t=0, the colors is unchanged. If t=1,
        the color becomes grey.

        >>> HexColor("C00").desaturate(t=0.5)
        '9B3232'
        """
        grey = HexColor.fromRgb((int(self.lightness()),) * 3)
        return self.interpolate(grey, t=t)

    def interpolate(self, other: 'HexColor', t: float):
        """
        >>> HexColor("F00").interpolate(HexColor("000"), t=0)
        'FF0000'
        >>> HexColor("F00").interpolate(HexColor("000"), t=1)
        '000000'
        >>> HexColor("888").interpolate(HexColor("000"), t=0.5)
        '636363'
        """
        gamma = 2.2
        aaa, bbb = [
            [channel ** gamma for channel in color.rgb]
            for color in [self, other]
        ]
        ccc = [a * (1.0 - t) + t * b for a, b in zip(aaa, bbb)]
        rgbResult = tuple(round(c ** (1/gamma)) for c in ccc)
        return HexColor.fromRgb(cast(Tuple[int, int, int], rgbResult))

    def distanceTo(self, other: "HexColor"):
        return sum((a - b) ** 2 for a, b in zip(self.rgb, other.rgb))

    def approxName(self):
        """
        >>> HexColor.ternColorDict['red'].approxName()
        'red'
        >>> HexColor("00EE00").approxName()
        'green'
        >>> HexColor("707070").approxName()
        'grey'
        >>> HexColor("303030").approxName()
        'dark_grey'
        """
        colorWithWeightedDistances = [
            (self.distanceTo(color), name)
            for name, color in HexColor.ternColorDict.items()
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
    purple=HexColor("9060FF"),
    orange=HexColor("FF8000"),
    brown=HexColor("7C4F2B"),
    grey=HexColor("808080"),
    black=HexColor("000000"),
    white=HexColor("FFFFFF"),
    dark_grey=HexColor("404040"),
    light_grey=HexColor("C0C0C0"),
)

HexColor.ternColorDict = dict(
    (key, value.desaturate())
    for key, value in HexColor.vividColorDict.items()
)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
