def clamp(minValue: int, maxValue: int):
    if minValue > maxValue:
        raise ValueError()

    def clampFunction(value):
        return min(maxValue, max(minValue, value))

    return clampFunction