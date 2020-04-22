from typing import List

from ... import answer as a
from ... import lexicalFragment as lxf
from ...context import Context
from .. import reaction as rt
from .. import recipe as rc
from ..lemmaData import LemmaData
from ..rule import fragmentDeck as deck
from ..rule import rule as ru
from ..rule import sentencePattern as sp
from ..util.digitToWord import digitToWord
from ..util.formatEnumeration import formatEnumeration
from ..util.formatListing import formatListing

# Who is a Kirin?
# :1_Lwho_Upron_Nx_Rroot_FPronType=Int_==.
# :2_Lbe_Uaux_N1_Rcop_FMood=Ind_FNumber=Sing_FPerson=3_FTense=Pres_FVerbForm=Fin_<.
# :3_La_Udet_Nx_Rdet_FDefinite=Ind_FPronType=Art_>.
# :4_Lkirin_Unoun_N1_Rnsubj_FNumber=Sing_<=.
# :5_L?_Upunct_Nx_Rpunct_F_<--.


template0 = """
I know what a {className} is but I don't know any.
""".lstrip()

template1 = """
I know only one {className}: {nameList[0]}.
""".lstrip()

template2 = """
I know just two {className}s: {nameEnumeration}.
""".lstrip()

templateUpTo10 = """
I know {countWord} {className}s: {nameEnumeration}.
""".lstrip()

templateMore = """
I know {countWord} {className}s. They are:
{nameBlock}
""".lstrip()

templateCountList = [
    template0,
    template1,
    template2,
]


def selectTemplate(count: int):
    if count <= 2:
        return templateCountList[count]
    elif count <= 10:
        return templateUpTo10
    else:
        return templateMore


class IndividualOfClassReaction(rt.Reaction):
    def react(self, context: Context, lemmaData: LemmaData, answer: a.Answer):
        classList: List[str] = lemmaData

        nameList = [
            name.replace("_", " ")
            for name in context.ontology.classIndividualQuery(classList)
        ]
        nameBlock = formatListing(nameList)

        count = len(nameList)

        template = selectTemplate(count)

        answer.text += template.format(
            className=" ".join(classList).replace("_", " ").lower(),
            count=count,
            countWord=digitToWord(count),
            nameBlock=nameBlock,
            nameEnumeration=formatEnumeration(nameList),
            nameList=nameList,
        )


class IndividualOfClassRecipeGroup:
    def createRecipeList(self):
        classReaction = IndividualOfClassReaction()

        return [
            rc.Recipe(
                classReaction,
                ru.Rule(
                    name="IndividualOfClass A",
                    shape="Who are the <C>s?",
                    fragmentList=[
                        deck.whoIs,
                        lxf.LexicalFragment(
                            kind="class", fragment=deck.nominal
                        ),
                    ],
                ),
            ),
        ]
