
from typing import List
from oxbot.datatype.pword import PWord


symbolMap = {
    -6: "<=-",
    -5: "<-=",
    -4: "<--",
    -3: "<=",
    -2: "<-",
    -1: "<",
    0: "==",
    1: ">",
    2: "->",
    3: "=>",
    4: "-->",
    5: "=->",
    6: "-=>",
}


def normalSentence(wordList: List[PWord]) -> str:
    normalWordList = []
    for word in wordList:
        normalWordList.append(normalWord(word))
    return " ".join(normalWordList)

def normalWord(word: PWord) -> str:
    diff = word.head - int(word.id)
    if word.head == 0:
        diff = 0
    symbol = symbolMap.get(diff)
    number = "x"
    for piece in word.feats.split("|"):
        partList = piece.split("=")
        if len(partList) != 2:
            continue
        left, right = partList
        if left == "Number":
            if right == "Plur":
                number = "2"
            if right == "Sing":
                number = "1"

    w = word
    upos = w.upos.lower()
    return f":{w.id}_L{w.lemma}_U{upos}_N{number}_R{w.deprel}_F{w.feats}_{symbol}."