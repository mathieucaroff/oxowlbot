import logging
import re
from itertools import chain, cycle

from ... import answer as a
from ... import context as c
from ... import lexicalFragment as lxf
from .. import reaction as rt
from .. import recipe as rc
from ..color.colorObj import ColorObj
from ..color.hexColor import HexColor
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru
from ..util.formatEnumeration import formatEnumeration
from ..util.pronoun import Pronoun


class KnowledgeReaction(rt.Reaction):
    async def react(
        self, context: "c.Context", lemmaData: LemmaData, answer: a.Answer
    ):
        individualName = lemmaData[0]
        info = context.ontology.individualInfoQuery(individualName)

        genderList = []
        classList = []
        friendList = []
        colorObj = ColorObj()
        otherRelationDict = {}

        for relation, targetRaw in info.relationList:
            target = targetRaw.replace("_", " ")
            if relation == "type":
                if target in ["Male", "Female"]:
                    genderList.append(target.lower())
                else:
                    classList.append(target.lower())
            elif relation == "friend_with":
                friendList.append(target)
            elif "color" in relation:
                if target == "":
                    logging.warn(f"empty {individualName} {relation} value")
                    continue
                setattr(colorObj, relation, HexColor(target))
            else:
                otherRelationDict.setdefault(relation, []).append(target)

        gender = genderList[0] if len(genderList) == 1 else "other"

        p = Pronoun(
            *dict(male="he his is has", female="she her is has")
            .get(gender, "they their are have")
            .split()
        )

        it_be = chain(
            [f"{individualName} is"], cycle([p.They_be, f"{p.They_be} also"])
        )

        text = ""

        if len(genderList) + len(classList) > 0:
            genderQualification = " and ".join(genderList)
            classQualification = " and ".join(classList)

            qualification = " ".join([genderQualification, classQualification])

            text += f"{next(it_be)} a {qualification}. "

        colorInfo = colorObj.tell(p)
        if colorInfo is not None:
            text += colorInfo

        if len(friendList) > 0:
            text += (
                f"{next(it_be)} friend with {formatEnumeration(friendList)}. "
            )

        for relation, targetList in otherRelationDict.items():
            text += (
                f"{next(it_be)} {relation} {formatEnumeration(targetList)}. "
            )

        text = re.sub(r"(?<!\s)\s+$", "\n", text)

        answer.text += text.replace("_", " ")


class KnowledgeRecipeGroup:
    def createRecipeList(self):
        knowledgeReaction = KnowledgeReaction()

        individualFragment = lxf.LexicalFragment(
            kind="individual", fragment=deck.nominal
        )

        return [
            rc.Recipe(
                knowledgeReaction,
                ru.Rule(
                    name="Knowledge A",
                    shape="Who is <I>?",
                    fragmentList=[deck.whoIs, individualFragment],
                ),
            ),
            rc.Recipe(
                knowledgeReaction,
                ru.Rule(
                    name="Knowledge B",
                    shape="What do you know about <I>?",
                    fragmentList=[deck.whatAbout, individualFragment],
                ),
            ),
        ]
