from ... import answer as a
from ...recipe import reaction as rt
from ...recipe import recipe as rc
from ... import lexicalFragment as lxf
from ...normal.normal import Normal
from ..rule import fragmentDeck as deck
from ..rule import sentencePattern as sp
from ..rule.rule import Rule


# pattern = Pattern(r"^<Lwh(?:o|ich),Upron>~<Lbe,Rcop>(~<!!Rnsubj>~<!!Rnsubj>)$")
pattern = sp.SentencePattern([deck.whoIs, deck.nominal])


class KnowledgeReaction(rt.Reaction):
    def react(self, normal: Normal) -> a.Answer: ...


class KnowledgeRecipeGroup:
    def createRecipeList(self):
        knowledgeReaction = KnowledgeReaction()

        return [
            rc.Recipe(Rule(
                name="Knowledge A",
                shape="Who is <I>?",
                fragmentList=[
                    deck.whoIs,
                    lxf.LexicalFragment(
                        kind="individual",
                        fragment=deck.nominal
                    ),
                ],
            ), knowledgeReaction),
        ]


# def knowledgeRecipeOld(
#     wordList: List[PWord],
#     normalSentence: str,
#     lexic: Lexic,
#     answer: Answer,
# ):
    # yield "Syntax Analysis"

    # match = pattern.match(normalSentence)

    # if match == None:
    #     yield False
    # yield True

    # id = int(match[1])
    # individualDesignation = wordList[id - 1]

    # yield "Shape"

    # shape = "Who is <I>?"
    # yield shape

    # yield "Lexical Analysis"

    # ok = True
    # individualList: List[str] = []
    # try:
    #     individualList = lexic.getIndividualList(individualDesignation)
    # except KeyError:
    #     ok = False
    # yield ok

    # yield from self.rule.run(
    #     wordList,
    #     normalSentence,
    #     lexic,
    #     answer,
    # )
