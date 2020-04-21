digitToString = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
}

def digitToWord(d: int):
    a = abs(d)
    m = '-' if d < 0 else ''
    return m + digitToString.get(a, str(a))