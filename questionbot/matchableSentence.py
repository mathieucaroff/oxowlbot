import logging
from typing import List

from .stanza.pword import PWord

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


def matchableSentence(wordList: List[PWord]) -> str:
    matchableWordList = []
    for word in wordList:
        matchableWordList.append(matchableWord(word))
    return " ".join(matchableWordList)


def matchableWord(word: PWord) -> str:
    diff = word.head - int(word.id)
    if word.head == 0:
        diff = 0
    symbol = symbolMap.get(diff)
    number = "x"
    hintString = ""
    pastHint = 0

    for piece in word.feats.split("|"):
        if piece == "Number=Plur":
            number = "2"
        if piece == "Number=Sing":
            number = "1"
        if piece == "VerbForm=Part":
            pastHint += 1
        if piece == "Tense=Past":
            pastHint += 1

    if pastHint >= 2:
        hintString += "_Hpast"

    w = word
    upos = w.upos.lower()
    feats = w.feats.replace("|", "_F").replace(":", "+")
    deprel = w.deprel.replace(':', '+')
    result = f":{w.id}_L{w.lemma}_U{upos}_N{number}_R{deprel}{hintString}_F{feats}_{symbol}."

    if "." in result[1:-1] or ":" in result[1:-1]:
        logging.error(f"bad (:.) matchableWord: {result}")
        result = ":" + result.replace(":", "").replace(".", "") + "."

    return result
