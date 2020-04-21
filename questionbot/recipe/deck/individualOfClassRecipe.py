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

# Who is a Kirin?
# :1_Lwho_Upron_Nx_Rroot_FPronType=Int_==.
# :2_Lbe_Uaux_N1_Rcop_FMood=Ind_FNumber=Sing_FPerson=3_FTense=Pres_FVerbForm=Fin_<.
# :3_La_Udet_Nx_Rdet_FDefinite=Ind_FPronType=Art_>.
# :4_Lkirin_Unoun_N1_Rnsubj_FNumber=Sing_<=.
# :5_L?_Upunct_Nx_Rpunct_F_<--.


template0 = """
I know what a {className} is but I don't know any of them.
""".strip()

template1 = """
I know only one {className}: {nameList[0]}.
""".strip()

template2 = """
I know just two {className}s: {nameList[0]} and {nameList[1]}.
""".strip()

templateUpTo10 = """
I know {countWord} {className}s: {nameEnumerationWithoutLast} and {nameList[-1]}.
""".strip()

templateMore = """
I know {countWord} {className}s. They are:
{nameBlock}
""".strip()

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
        className: str = lemmaData[0]

        nameList = [
            name.replace("_", " ")
            for name in context.ontology.classIndividualQuery(className)
        ]
        nameBlock = "\n".join("- " + w for w in nameList)

        nameEnumeration = ", ".join(nameList)

        count = len(nameList)

        template = selectTemplate(count)

        nameEnumerationWithoutLast = ", ".join(nameList[:-1])

        answer.text += template.format(
            className=className.replace("_", " "),
            count=count,
            countWord=digitToWord(count),
            nameBlock=nameBlock,
            nameEnumeration=nameEnumeration,
            nameEnumerationWithoutLast=nameEnumerationWithoutLast,
            nameList=nameList,
        )


class IndividualOfClassRecipeGroup:
    def createRecipeList(self):
        knowledgeReaction = IndividualOfClassReaction()

        return [
            rc.Recipe(
                knowledgeReaction,
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
