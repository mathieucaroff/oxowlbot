# from typing import List

# if 1 == 0:
#     from ..lexic import Lexic
#     from ..stanza.pword import PWord
#     from .pattern.pattern import Pattern


# pattern = Pattern(r"^<Lwh(?:o|ich),Upron>~<Lbe,Rcop>~<!!Rnsubj>$")


# def individualOfClassRecipeGroup(
#     wordList: List[PWord],
#     normalSentence: str,
#     lexic: Lexic,
# ):
#     """
#     List the individuals of a class.
#     """
#     yield "Syntax Analysis"

#     match = pattern.match(normalSentence)

#     if match == None:
#         yield False
#     yield True

#     id = int(match[1])
#     classDesignation = wordList[id - 1]

#     yield "Shape"

#     shape = "Who is <C>?"
#     yield shape

#     yield "Lexical Analysis"

#     ...