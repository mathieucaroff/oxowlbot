
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

    def obtainLexicalTerm(self, extract: List[str], lexic: 'lx.Lexic', answer: a.Answer):
        if self.kind == 'individual':
            name = " ".join(extract)

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
            name = " ".join(extract)
            return lexic.getClass(name)
        if self.kind == 'relation':
            relationNameList = extract
            return [lexic.getIndividualList(name) for name in relationNameList]
