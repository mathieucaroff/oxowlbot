
from . import answer as a
from .recipe.rule.sentencePattern import ActiveFragment
from typing import List, Literal
from . import lexic as lx


LexicalFragmentKind = Literal['class', 'individual', 'relation']
class LexicalFragment(ActiveFragment):
    kind: LexicalFragmentKind

    def __init__(self, kind: LexicalFragmentKind, fragment: ActiveFragment):
        super().__init__(fragment.overview, fragment.detail)
        self.kind = kind

    def obtainLexicalChunk(self, activeExtract: List[str], lexic: 'lx.Lexic', answer: a.Answer):
        if self.kind == 'individual':
            name = " ".join(activeExtract)

            ambiguityList = lexic.getIndividualList(name)

            individual = ambiguityList[0]

            if len(ambiguityList) > 1:
                notice = (
                    "The name \"{name}\" is lexically ambiguous. It designates the following individuals:\n"
                    "- {individualList}\n"
                    'I selected the first of them "{choice}" and worked from there\n\n'
                ).format(
                    name=name,
                    individualList="\n- ".join(ambiguityList),
                    choice=individual,
                )

                answer.warning += notice
            return individual
        if self.kind == 'class':
            name = " ".join(activeExtract)
            return lexic.getClass(name)
        if self.kind == 'relation':
            relationNameList = activeExtract
            return [*map(lexic.getRelation, relationNameList)]

        raise RuntimeError()
