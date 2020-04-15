"""
This type stub file was generated by pyright.
"""

import sys
from collections import OrderedDict
from pyparsing import TokenConverter, Word, nums  # type: ignore
from typing import Any, Optional

DEBUG = True
DEBUG = False
if DEBUG: ...

def value(ctx, val, variables: bool = ..., errors: bool = ...):
    """
    utility function for evaluating something...

    Variables will be looked up in the context
    Normally, non-bound vars is an error,
    set variables=True to return unbound vars

    Normally, an error raises the error,
    set errors=True to return error

    """
    ...

class ParamValue(object):
    """
    The result of parsing a Param
    This just keeps the name/value
    All cleverness is in the CompValue
    """

    def __init__(self, name, tokenList, isList):
        self.isList = ...
        self.name = ...
        self.tokenList = ...
    def __str__(self): ...

class Param(TokenConverter):
    """
    A pyparsing token for labelling a part of the parse-tree
    if isList is true repeat occurrences of ParamList have
    their values merged in a list
    """

    def __init__(self, name, expr, isList: bool = ...):
        self.name = ...
        self.isList = ...
    def postParse2(self, tokenList): ...

class ParamList(Param):
    """
    A shortcut for a Param with isList=True
    """

    def __init__(self, name, expr): ...

class plist(list):
    """this is just a list, but we want our own type to check for"""

    ...

class CompValue(OrderedDict):
    """
    The result of parsing a Comp
    Any included Params are avaiable as Dict keys
    or as attributes

    """

    def __init__(self, name, **values):
        self.name = ...
    def clone(self): ...
    def __str__(self): ...
    def __repr__(self): ...
    def _value(self, val, variables: bool = ..., errors: bool = ...): ...
    def __getitem__(self, a): ...
    def get(self, a, variables: bool = ..., errors: bool = ...): ...
    def __getattr__(self, a): ...

class Expr(CompValue):
    """
    A CompValue that is evaluatable
    """

    def __init__(self, name, evalfn: Optional[Any] = ..., **values): ...
    def eval(self, ctx=...): ...

class Comp(TokenConverter):
    """
    A pyparsing token for grouping together things with a label
    Any sub-tokens that are not Params will be ignored.

    Returns CompValue / Expr objects - depending on whether evalFn is set.
    """

    def __init__(self, name, expr):
        self.name = ...
        self.evalfn = ...
    def postParse(self, instring, loc, tokenList): ...
    def setEvalFn(self, evalfn):
        self.evalfn = ...

def prettify_parsetree(t, indent=..., depth=...): ...

if __name__ == "__main__":
    Number = Word(nums)
    Plus = Comp("plus", Param("a", Number) + "+" + Param("b", Number))
    r = Plus.parseString(sys.argv[1])
