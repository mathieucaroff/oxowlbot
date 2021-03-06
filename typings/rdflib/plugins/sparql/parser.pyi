"""
This type stub file was generated by pyright.
"""

from typing import Any

import sys
import re
import rdflib  # type: ignore

rdflib: Any
from pyparsing import CaselessKeyword as Keyword, Combine, Forward, Group, Literal, OneOrMore, Optional, Regex, Suppress, ZeroOrMore, delimitedList  # type: ignore
from .parserutils import Comp, Param, ParamList
from . import operators as op

"""
SPARQL 1.1 Parser

based on pyparsing
"""
DEBUG = False

def neg(literal): ...
def setLanguage(terms): ...
def setDataType(terms): ...
def expandTriples(terms):
    """
    Expand ; and , syntax for repeat predicates, subjects
    """
    ...

def expandBNodeTriples(terms):
    """
    expand [ ?p ?o ] syntax for implicit bnodes
    """
    ...

def expandCollection(terms):
    """
    expand ( 1 2 3 ) notation for collections
    """
    ...

IRIREF = Combine(
    Suppress("<")
    + Regex(r'[^<>"{}|^`\\%s]*' % "".join("\\x%02X" % i for i in range(33)))
    + Suppress(">")
)
if sys.maxunicode == 65535:
    PN_CHARS_BASE_re = "A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD"
else:
    PN_CHARS_BASE_re = "A-Za-z\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u02FF\u0370-\u037D\u037F-\u1FFF\u200C-\u200D\u2070-\u218F\u2C00-\u2FEF\u3001-\uD7FF\uF900-\uFDCF\uFDF0-\uFFFD\U00010000-\U000EFFFF"
PN_CHARS_U_re = "_" + PN_CHARS_BASE_re
PN_CHARS_re = "\\-0-9\u00B7\u0300-\u036F\u203F-\u2040" + PN_CHARS_U_re
PN_PREFIX = Regex(
    r"[%s](?:[%s\.]*[%s])?" % (PN_CHARS_BASE_re, PN_CHARS_re, PN_CHARS_re), flags=re.U
)
PNAME_NS = Optional(Param("prefix", PN_PREFIX)) + Suppress(":").leaveWhitespace()
PN_LOCAL_ESC_re = "\\\\[_~\\.\\-!$&\"'()*+,;=/?#@%]"
PERCENT_re = "%[0-9a-fA-F]{2}"
PLX_re = "(%s|%s)" % (PN_LOCAL_ESC_re, PERCENT_re)
PN_LOCAL = Regex(
    r"""([%(PN_CHARS_U)s:0-9]|%(PLX)s)
                     (([%(PN_CHARS)s\.:]|%(PLX)s)*
                      ([%(PN_CHARS)s:]|%(PLX)s) )?"""
    % dict(PN_CHARS_U=PN_CHARS_U_re, PN_CHARS=PN_CHARS_re, PLX=PLX_re),
    flags=re.X | re.UNICODE,
)

def _hexExpand(match): ...

PNAME_LN = PNAME_NS + Param("localname", PN_LOCAL.leaveWhitespace())
BLANK_NODE_LABEL = Regex(
    r"_:[0-9%s](?:[\.%s]*[%s])?" % (PN_CHARS_U_re, PN_CHARS_re, PN_CHARS_re), flags=re.U
)
VARNAME = Regex(
    "[%s0-9][%s0-9\u00B7\u0300-\u036F\u203F-\u2040]*" % (PN_CHARS_U_re, PN_CHARS_U_re),
    flags=re.U,
)
VAR1 = Combine(Suppress("?") + VARNAME)
VAR2 = Combine(Suppress("$") + VARNAME)
LANGTAG = Combine(Suppress("@") + Regex("[a-zA-Z]+(?:-[a-zA-Z0-9]+)*"))
INTEGER = Regex(r"[0-9]+")
EXPONENT_re = "[eE][+-]?[0-9]+"
DECIMAL = Regex(r"[0-9]*\.[0-9]+")
DOUBLE = Regex(r"[0-9]+\.[0-9]*%(e)s|\.([0-9])+%(e)s|[0-9]+%(e)s" % {"e": EXPONENT_re})
INTEGER_POSITIVE = Suppress("+") + INTEGER.copy().leaveWhitespace()
DECIMAL_POSITIVE = Suppress("+") + DECIMAL.copy().leaveWhitespace()
DOUBLE_POSITIVE = Suppress("+") + DOUBLE.copy().leaveWhitespace()
INTEGER_NEGATIVE = Suppress("-") + INTEGER.copy().leaveWhitespace()
DECIMAL_NEGATIVE = Suppress("-") + DECIMAL.copy().leaveWhitespace()
DOUBLE_NEGATIVE = Suppress("-") + DOUBLE.copy().leaveWhitespace()
STRING_LITERAL_LONG1 = Regex(r"'''((?:'|'')?(?:[^'\\]|\\['ntbrf\\]))*'''")
STRING_LITERAL_LONG2 = Regex(r'"""(?:(?:"|"")?(?:[^"\\]|\\["ntbrf\\]))*"""')
STRING_LITERAL1 = Regex(r"'(?:[^'\n\r\\]|\\['ntbrf\\])*'(?!')", flags=re.U)
STRING_LITERAL2 = Regex(r'"(?:[^"\n\r\\]|\\["ntbrf\\])*"(?!")', flags=re.U)
NIL = Literal("(") + ")"
ANON = Literal("[") + "]"
A = Literal("a")
BaseDecl = Comp("Base", Keyword("BASE") + Param("iri", IRIREF))
PrefixDecl = Comp("PrefixDecl", Keyword("PREFIX") + PNAME_NS + Param("iri", IRIREF))
Prologue = Group(ZeroOrMore(BaseDecl | PrefixDecl))
Var = VAR1 | VAR2
PrefixedName = Comp("pname", PNAME_LN | PNAME_NS)
iri = IRIREF | PrefixedName
String = STRING_LITERAL_LONG1 | STRING_LITERAL_LONG2 | STRING_LITERAL1 | STRING_LITERAL2
RDFLiteral = Comp(
    "literal",
    Param("string", String)
    + Optional(
        Param("lang", LANGTAG.leaveWhitespace())
        | Literal("^^").leaveWhitespace() + Param("datatype", iri).leaveWhitespace()
    ),
)
NumericLiteralPositive = DOUBLE_POSITIVE | DECIMAL_POSITIVE | INTEGER_POSITIVE
NumericLiteralNegative = DOUBLE_NEGATIVE | DECIMAL_NEGATIVE | INTEGER_NEGATIVE
NumericLiteralUnsigned = DOUBLE | DECIMAL | INTEGER
NumericLiteral = (
    NumericLiteralUnsigned | NumericLiteralPositive | NumericLiteralNegative
)
BooleanLiteral = Keyword("true").setParseAction(lambda: rdflib.Literal(True)) | Keyword(
    "false"
).setParseAction(lambda: rdflib.Literal(False))
BlankNode = BLANK_NODE_LABEL | ANON
GraphTerm = iri | RDFLiteral | NumericLiteral | BooleanLiteral | BlankNode | NIL
VarOrTerm = Var | GraphTerm
VarOrIri = Var | iri
GraphRef = Keyword("GRAPH") + Param("graphiri", iri)
GraphRefAll = (
    GraphRef
    | Param("graphiri", Keyword("DEFAULT"))
    | Param("graphiri", Keyword("NAMED"))
    | Param("graphiri", Keyword("ALL"))
)
GraphOrDefault = ParamList("graph", Keyword("DEFAULT")) | Optional(
    Keyword("GRAPH")
) + ParamList("graph", iri)
DataBlockValue = iri | RDFLiteral | NumericLiteral | BooleanLiteral | Keyword("UNDEF")
Verb = VarOrIri | A
VerbSimple = Var
Integer = INTEGER
TriplesNode = Forward()
TriplesNodePath = Forward()
GraphNode = VarOrTerm | TriplesNode
GraphNodePath = VarOrTerm | TriplesNodePath
PathMod = Literal("?") | "*" | "+"
PathOneInPropertySet = iri | A | Comp("InversePath", "^" + iri | A)
Path = Forward()
PathNegatedPropertySet = Comp(
    "PathNegatedPropertySet",
    ParamList("part", PathOneInPropertySet)
    | "("
    + Optional(
        ParamList("part", PathOneInPropertySet)
        + ZeroOrMore("|" + ParamList("part", PathOneInPropertySet))
    )
    + ")",
)
PathPrimary = (
    iri
    | A
    | Suppress("!") + PathNegatedPropertySet
    | Suppress("(") + Path + Suppress(")")
    | Comp("DistinctPath", Keyword("DISTINCT") + "(" + Param("part", Path) + ")")
)
PathElt = Comp(
    "PathElt",
    Param("part", PathPrimary) + Optional(Param("mod", PathMod.leaveWhitespace())),
)
PathEltOrInverse = PathElt | Suppress("^") + Comp(
    "PathEltOrInverse", Param("part", PathElt)
)
PathSequence = Comp(
    "PathSequence",
    ParamList("part", PathEltOrInverse)
    + ZeroOrMore("/" + ParamList("part", PathEltOrInverse)),
)
PathAlternative = Comp(
    "PathAlternative",
    ParamList("part", PathSequence) + ZeroOrMore("|" + ParamList("part", PathSequence)),
)
VerbPath = Path
ObjectPath = GraphNodePath
ObjectListPath = ObjectPath + ZeroOrMore("," + ObjectPath)
GroupGraphPattern = Forward()
Collection = Suppress("(") + OneOrMore(GraphNode) + Suppress(")")
CollectionPath = Suppress("(") + OneOrMore(GraphNodePath) + Suppress(")")
Object = GraphNode
ObjectList = Object + ZeroOrMore("," + Object)
PropertyListPathNotEmpty = VerbPath | VerbSimple + ObjectListPath + ZeroOrMore(
    ";" + Optional(VerbPath | VerbSimple + ObjectList)
)
PropertyListPath = Optional(PropertyListPathNotEmpty)
PropertyListNotEmpty = Verb + ObjectList + ZeroOrMore(";" + Optional(Verb + ObjectList))
PropertyList = Optional(PropertyListNotEmpty)
BlankNodePropertyList = Group(Suppress("[") + PropertyListNotEmpty + Suppress("]"))
BlankNodePropertyListPath = Group(
    Suppress("[") + PropertyListPathNotEmpty + Suppress("]")
)
TriplesSameSubject = VarOrTerm + PropertyListNotEmpty | TriplesNode + PropertyList
TriplesTemplate = Forward()
QuadsNotTriples = Comp(
    "QuadsNotTriples",
    Keyword("GRAPH") + Param("term", VarOrIri) + "{" + Optional(TriplesTemplate) + "}",
)
Quads = Comp(
    "Quads",
    Optional(TriplesTemplate)
    + ZeroOrMore(
        ParamList("quadsNotTriples", QuadsNotTriples)
        + Optional(Suppress("."))
        + Optional(TriplesTemplate)
    ),
)
QuadPattern = "{" + Param("quads", Quads) + "}"
QuadData = "{" + Param("quads", Quads) + "}"
TriplesSameSubjectPath = (
    VarOrTerm + PropertyListPathNotEmpty | TriplesNodePath + PropertyListPath
)
TriplesBlock = Forward()
MinusGraphPattern = Comp(
    "MinusGraphPattern", Keyword("MINUS") + Param("graph", GroupGraphPattern)
)
GroupOrUnionGraphPattern = Comp(
    "GroupOrUnionGraphPattern",
    ParamList("graph", GroupGraphPattern)
    + ZeroOrMore(Keyword("UNION") + ParamList("graph", GroupGraphPattern)),
)
Expression = Forward()
ExpressionList = NIL | Group(Suppress("(") + delimitedList(Expression) + Suppress(")"))
RegexExpression = Comp(
    "Builtin_REGEX",
    Keyword("REGEX")
    + "("
    + Param("text", Expression)
    + ","
    + Param("pattern", Expression)
    + Optional("," + Param("flags", Expression))
    + ")",
)
SubstringExpression = Comp(
    "Builtin_SUBSTR",
    Keyword("SUBSTR")
    + "("
    + Param("arg", Expression)
    + ","
    + Param("start", Expression)
    + Optional("," + Param("length", Expression))
    + ")",
).setEvalFn(op.Builtin_SUBSTR)
StrReplaceExpression = Comp(
    "Builtin_REPLACE",
    Keyword("REPLACE")
    + "("
    + Param("arg", Expression)
    + ","
    + Param("pattern", Expression)
    + ","
    + Param("replacement", Expression)
    + Optional("," + Param("flags", Expression))
    + ")",
).setEvalFn(op.Builtin_REPLACE)
ExistsFunc = Comp(
    "Builtin_EXISTS", Keyword("EXISTS") + Param("graph", GroupGraphPattern)
).setEvalFn(op.Builtin_EXISTS)
NotExistsFunc = Comp(
    "Builtin_NOTEXISTS",
    Keyword("NOT") + Keyword("EXISTS") + Param("graph", GroupGraphPattern),
).setEvalFn(op.Builtin_EXISTS)
_Distinct = Optional(Keyword("DISTINCT"))
_AggregateParams = "(" + Param("distinct", _Distinct) + Param("vars", Expression) + ")"
Aggregate = (
    Comp(
        "Aggregate_Count",
        Keyword("COUNT")
        + "("
        + Param("distinct", _Distinct)
        + Param("vars", "*" | Expression)
        + ")",
    )
    | Comp("Aggregate_Sum", Keyword("SUM") + _AggregateParams)
    | Comp("Aggregate_Min", Keyword("MIN") + _AggregateParams)
    | Comp("Aggregate_Max", Keyword("MAX") + _AggregateParams)
    | Comp("Aggregate_Avg", Keyword("AVG") + _AggregateParams)
    | Comp("Aggregate_Sample", Keyword("SAMPLE") + _AggregateParams)
    | Comp(
        "Aggregate_GroupConcat",
        Keyword("GROUP_CONCAT")
        + "("
        + Param("distinct", _Distinct)
        + Param("vars", Expression)
        + Optional(";" + Keyword("SEPARATOR") + "=" + Param("separator", String))
        + ")",
    )
)
BuiltInCall = (
    Aggregate
    | Comp(
        "Builtin_STR", Keyword("STR") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_STR)
    | Comp(
        "Builtin_LANG", Keyword("LANG") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_LANG)
    | Comp(
        "Builtin_LANGMATCHES",
        Keyword("LANGMATCHES")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_LANGMATCHES)
    | Comp(
        "Builtin_DATATYPE", Keyword("DATATYPE") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_DATATYPE)
    | Comp("Builtin_BOUND", Keyword("BOUND") + "(" + Param("arg", Var) + ")").setEvalFn(
        op.Builtin_BOUND
    )
    | Comp(
        "Builtin_IRI", Keyword("IRI") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_IRI)
    | Comp(
        "Builtin_URI", Keyword("URI") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_IRI)
    | Comp(
        "Builtin_BNODE", Keyword("BNODE") + "(" + Param("arg", Expression) + ")" | NIL
    ).setEvalFn(op.Builtin_BNODE)
    | Comp("Builtin_RAND", Keyword("RAND") + NIL).setEvalFn(op.Builtin_RAND)
    | Comp(
        "Builtin_ABS", Keyword("ABS") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_ABS)
    | Comp(
        "Builtin_CEIL", Keyword("CEIL") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_CEIL)
    | Comp(
        "Builtin_FLOOR", Keyword("FLOOR") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_FLOOR)
    | Comp(
        "Builtin_ROUND", Keyword("ROUND") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_ROUND)
    | Comp(
        "Builtin_CONCAT", Keyword("CONCAT") + Param("arg", ExpressionList)
    ).setEvalFn(op.Builtin_CONCAT)
    | SubstringExpression
    | Comp(
        "Builtin_STRLEN", Keyword("STRLEN") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_STRLEN)
    | StrReplaceExpression
    | Comp(
        "Builtin_UCASE", Keyword("UCASE") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_UCASE)
    | Comp(
        "Builtin_LCASE", Keyword("LCASE") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_LCASE)
    | Comp(
        "Builtin_ENCODE_FOR_URI",
        Keyword("ENCODE_FOR_URI") + "(" + Param("arg", Expression) + ")",
    ).setEvalFn(op.Builtin_ENCODE_FOR_URI)
    | Comp(
        "Builtin_CONTAINS",
        Keyword("CONTAINS")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_CONTAINS)
    | Comp(
        "Builtin_STRSTARTS",
        Keyword("STRSTARTS")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRSTARTS)
    | Comp(
        "Builtin_STRENDS",
        Keyword("STRENDS")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRENDS)
    | Comp(
        "Builtin_STRBEFORE",
        Keyword("STRBEFORE")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRBEFORE)
    | Comp(
        "Builtin_STRAFTER",
        Keyword("STRAFTER")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRAFTER)
    | Comp(
        "Builtin_YEAR", Keyword("YEAR") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_YEAR)
    | Comp(
        "Builtin_MONTH", Keyword("MONTH") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_MONTH)
    | Comp(
        "Builtin_DAY", Keyword("DAY") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_DAY)
    | Comp(
        "Builtin_HOURS", Keyword("HOURS") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_HOURS)
    | Comp(
        "Builtin_MINUTES", Keyword("MINUTES") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_MINUTES)
    | Comp(
        "Builtin_SECONDS", Keyword("SECONDS") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_SECONDS)
    | Comp(
        "Builtin_TIMEZONE", Keyword("TIMEZONE") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_TIMEZONE)
    | Comp(
        "Builtin_TZ", Keyword("TZ") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_TZ)
    | Comp("Builtin_NOW", Keyword("NOW") + NIL).setEvalFn(op.Builtin_NOW)
    | Comp("Builtin_UUID", Keyword("UUID") + NIL).setEvalFn(op.Builtin_UUID)
    | Comp("Builtin_STRUUID", Keyword("STRUUID") + NIL).setEvalFn(op.Builtin_STRUUID)
    | Comp(
        "Builtin_MD5", Keyword("MD5") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_MD5)
    | Comp(
        "Builtin_SHA1", Keyword("SHA1") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_SHA1)
    | Comp(
        "Builtin_SHA256", Keyword("SHA256") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_SHA256)
    | Comp(
        "Builtin_SHA384", Keyword("SHA384") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_SHA384)
    | Comp(
        "Builtin_SHA512", Keyword("SHA512") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_SHA512)
    | Comp(
        "Builtin_COALESCE", Keyword("COALESCE") + Param("arg", ExpressionList)
    ).setEvalFn(op.Builtin_COALESCE)
    | Comp(
        "Builtin_IF",
        Keyword("IF")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ","
        + Param("arg3", Expression)
        + ")",
    ).setEvalFn(op.Builtin_IF)
    | Comp(
        "Builtin_STRLANG",
        Keyword("STRLANG")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRLANG)
    | Comp(
        "Builtin_STRDT",
        Keyword("STRDT")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_STRDT)
    | Comp(
        "Builtin_sameTerm",
        Keyword("sameTerm")
        + "("
        + Param("arg1", Expression)
        + ","
        + Param("arg2", Expression)
        + ")",
    ).setEvalFn(op.Builtin_sameTerm)
    | Comp(
        "Builtin_isIRI", Keyword("isIRI") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_isIRI)
    | Comp(
        "Builtin_isURI", Keyword("isURI") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_isIRI)
    | Comp(
        "Builtin_isBLANK", Keyword("isBLANK") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_isBLANK)
    | Comp(
        "Builtin_isLITERAL", Keyword("isLITERAL") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_isLITERAL)
    | Comp(
        "Builtin_isNUMERIC", Keyword("isNUMERIC") + "(" + Param("arg", Expression) + ")"
    ).setEvalFn(op.Builtin_isNUMERIC)
    | RegexExpression
    | ExistsFunc
    | NotExistsFunc
)
ArgList = (
    NIL
    | "("
    + Param("distinct", _Distinct)
    + delimitedList(ParamList("expr", Expression))
    + ")"
)
iriOrFunction = (
    Comp("Function", Param("iri", iri) + ArgList).setEvalFn(op.Function) | iri
)
FunctionCall = Comp("Function", Param("iri", iri) + ArgList).setEvalFn(op.Function)
BrackettedExpression = Suppress("(") + Expression + Suppress(")")
PrimaryExpression = (
    BrackettedExpression
    | BuiltInCall
    | iriOrFunction
    | RDFLiteral
    | NumericLiteral
    | BooleanLiteral
    | Var
)
UnaryExpression = (
    Comp("UnaryNot", "!" + Param("expr", PrimaryExpression)).setEvalFn(op.UnaryNot)
    | Comp("UnaryPlus", "+" + Param("expr", PrimaryExpression)).setEvalFn(op.UnaryPlus)
    | Comp("UnaryMinus", "-" + Param("expr", PrimaryExpression)).setEvalFn(
        op.UnaryMinus
    )
    | PrimaryExpression
)
MultiplicativeExpression = Comp(
    "MultiplicativeExpression",
    Param("expr", UnaryExpression)
    + ZeroOrMore(
        ParamList("op", "*") + ParamList("other", UnaryExpression)
        | ParamList("op", "/") + ParamList("other", UnaryExpression)
    ),
).setEvalFn(op.MultiplicativeExpression)
AdditiveExpression = Comp(
    "AdditiveExpression",
    Param("expr", MultiplicativeExpression)
    + ZeroOrMore(
        ParamList("op", "+") + ParamList("other", MultiplicativeExpression)
        | ParamList("op", "-") + ParamList("other", MultiplicativeExpression)
    ),
).setEvalFn(op.AdditiveExpression)
NumericExpression = AdditiveExpression
RelationalExpression = Comp(
    "RelationalExpression",
    Param("expr", NumericExpression)
    + Optional(
        Param("op", "=") + Param("other", NumericExpression)
        | Param("op", "!=") + Param("other", NumericExpression)
        | Param("op", "<") + Param("other", NumericExpression)
        | Param("op", ">") + Param("other", NumericExpression)
        | Param("op", "<=") + Param("other", NumericExpression)
        | Param("op", ">=") + Param("other", NumericExpression)
        | Param("op", Keyword("IN")) + Param("other", ExpressionList)
        | Param(
            "op",
            Combine(Keyword("NOT") + Keyword("IN"), adjacent=False, joinString=" "),
        )
        + Param("other", ExpressionList)
    ),
).setEvalFn(op.RelationalExpression)
ValueLogical = RelationalExpression
ConditionalAndExpression = Comp(
    "ConditionalAndExpression",
    Param("expr", ValueLogical) + ZeroOrMore("&&" + ParamList("other", ValueLogical)),
).setEvalFn(op.ConditionalAndExpression)
ConditionalOrExpression = Comp(
    "ConditionalOrExpression",
    Param("expr", ConditionalAndExpression)
    + ZeroOrMore("||" + ParamList("other", ConditionalAndExpression)),
).setEvalFn(op.ConditionalOrExpression)
Constraint = BrackettedExpression | BuiltInCall | FunctionCall
Filter = Comp("Filter", Keyword("FILTER") + Param("expr", Constraint))
SourceSelector = iri
DefaultGraphClause = SourceSelector
NamedGraphClause = Keyword("NAMED") + Param("named", SourceSelector)
DatasetClause = Comp(
    "DatasetClause",
    Keyword("FROM") + Param("default", DefaultGraphClause) | NamedGraphClause,
)
GroupCondition = (
    BuiltInCall
    | FunctionCall
    | Comp(
        "GroupAs",
        "("
        + Param("expr", Expression)
        + Optional(Keyword("AS") + Param("var", Var))
        + ")",
    )
    | Var
)
GroupClause = Comp(
    "GroupClause",
    Keyword("GROUP")
    + Keyword("BY")
    + OneOrMore(ParamList("condition", GroupCondition)),
)
_Silent = Optional(Param("silent", Keyword("SILENT")))
Load = Comp(
    "Load",
    Keyword("LOAD")
    + _Silent
    + Param("iri", iri)
    + Optional(Keyword("INTO") + GraphRef),
)
Clear = Comp("Clear", Keyword("CLEAR") + _Silent + GraphRefAll)
Drop = Comp("Drop", Keyword("DROP") + _Silent + GraphRefAll)
Create = Comp("Create", Keyword("CREATE") + _Silent + GraphRef)
Add = Comp(
    "Add", Keyword("ADD") + _Silent + GraphOrDefault + Keyword("TO") + GraphOrDefault
)
Move = Comp(
    "Move", Keyword("MOVE") + _Silent + GraphOrDefault + Keyword("TO") + GraphOrDefault
)
Copy = Comp(
    "Copy", Keyword("COPY") + _Silent + GraphOrDefault + Keyword("TO") + GraphOrDefault
)
InsertData = Comp("InsertData", Keyword("INSERT") + Keyword("DATA") + QuadData)
DeleteData = Comp("DeleteData", Keyword("DELETE") + Keyword("DATA") + QuadData)
DeleteWhere = Comp("DeleteWhere", Keyword("DELETE") + Keyword("WHERE") + QuadPattern)
DeleteClause = Comp("DeleteClause", Keyword("DELETE") + QuadPattern)
InsertClause = Comp("InsertClause", Keyword("INSERT") + QuadPattern)
UsingClause = Comp(
    "UsingClause",
    Keyword("USING") + Param("default", iri) | Keyword("NAMED") + Param("named", iri),
)
Modify = Comp(
    "Modify",
    Optional(Keyword("WITH") + Param("withClause", iri))
    + Param("delete", DeleteClause)
    + Optional(Param("insert", InsertClause))
    | Param("insert", InsertClause)
    + ZeroOrMore(ParamList("using", UsingClause))
    + Keyword("WHERE")
    + Param("where", GroupGraphPattern),
)
Update1 = (
    Load
    | Clear
    | Drop
    | Add
    | Move
    | Copy
    | Create
    | InsertData
    | DeleteData
    | DeleteWhere
    | Modify
)
InlineDataOneVar = (
    ParamList("var", Var) + "{" + ZeroOrMore(ParamList("value", DataBlockValue)) + "}"
)
InlineDataFull = (
    NIL
    | "("
    + ZeroOrMore(ParamList("var", Var))
    + ")"
    + "{"
    + ZeroOrMore(
        ParamList(
            "value",
            Group(Suppress("(") + ZeroOrMore(DataBlockValue) + Suppress(")") | NIL),
        )
    )
    + "}"
)
DataBlock = InlineDataOneVar | InlineDataFull
ValuesClause = Optional(
    Param("valuesClause", Comp("ValuesClause", Keyword("VALUES") + DataBlock))
)
ConstructTriples = Forward()
ConstructTemplate = Suppress("{") + Optional(ConstructTriples) + Suppress("}")
OptionalGraphPattern = Comp(
    "OptionalGraphPattern", Keyword("OPTIONAL") + Param("graph", GroupGraphPattern)
)
GraphGraphPattern = Comp(
    "GraphGraphPattern",
    Keyword("GRAPH") + Param("term", VarOrIri) + Param("graph", GroupGraphPattern),
)
ServiceGraphPattern = Comp(
    "ServiceGraphPattern",
    Keyword("SERVICE")
    + _Silent
    + Param("term", VarOrIri)
    + Param("graph", GroupGraphPattern),
)
Bind = Comp(
    "Bind",
    Keyword("BIND")
    + "("
    + Param("expr", Expression)
    + Keyword("AS")
    + Param("var", Var)
    + ")",
)
InlineData = Comp("InlineData", Keyword("VALUES") + DataBlock)
GraphPatternNotTriples = (
    GroupOrUnionGraphPattern
    | OptionalGraphPattern
    | MinusGraphPattern
    | GraphGraphPattern
    | ServiceGraphPattern
    | Filter
    | Bind
    | InlineData
)
GroupGraphPatternSub = Comp(
    "GroupGraphPatternSub",
    Optional(ParamList("part", Comp("TriplesBlock", TriplesBlock)))
    + ZeroOrMore(
        ParamList("part", GraphPatternNotTriples)
        + Optional(".")
        + Optional(ParamList("part", Comp("TriplesBlock", TriplesBlock)))
    ),
)
HavingCondition = Constraint
HavingClause = Comp(
    "HavingClause",
    Keyword("HAVING") + OneOrMore(ParamList("condition", HavingCondition)),
)
OrderCondition = Comp(
    "OrderCondition",
    Param("order", Keyword("ASC") | Keyword("DESC"))
    + Param("expr", BrackettedExpression)
    | Param("expr", Constraint | Var),
)
OrderClause = Comp(
    "OrderClause",
    Keyword("ORDER")
    + Keyword("BY")
    + OneOrMore(ParamList("condition", OrderCondition)),
)
LimitClause = Keyword("LIMIT") + Param("limit", INTEGER)
OffsetClause = Keyword("OFFSET") + Param("offset", INTEGER)
LimitOffsetClauses = Comp(
    "LimitOffsetClauses",
    LimitClause + Optional(OffsetClause) | OffsetClause + Optional(LimitClause),
)
SolutionModifier = (
    Optional(Param("groupby", GroupClause))
    + Optional(Param("having", HavingClause))
    + Optional(Param("orderby", OrderClause))
    + Optional(Param("limitoffset", LimitOffsetClauses))
)
SelectClause = (
    Keyword("SELECT")
    + Optional(Param("modifier", Keyword("DISTINCT") | Keyword("REDUCED")))
    + OneOrMore(
        ParamList(
            "projection",
            Comp(
                "vars",
                Param("var", Var)
                | Literal("(")
                + Param("expr", Expression)
                + Keyword("AS")
                + Param("evar", Var)
                + ")",
            ),
        )
    )
    | "*"
)
WhereClause = Optional(Keyword("WHERE")) + Param("where", GroupGraphPattern)
SubSelect = Comp(
    "SubSelect", SelectClause + WhereClause + SolutionModifier + ValuesClause
)
SelectQuery = Comp(
    "SelectQuery",
    SelectClause
    + ZeroOrMore(ParamList("datasetClause", DatasetClause))
    + WhereClause
    + SolutionModifier
    + ValuesClause,
)
ConstructQuery = Comp(
    "ConstructQuery",
    Keyword("CONSTRUCT")
    + ConstructTemplate
    + ZeroOrMore(ParamList("datasetClause", DatasetClause))
    + WhereClause
    + SolutionModifier
    + ValuesClause
    | ZeroOrMore(ParamList("datasetClause", DatasetClause))
    + Keyword("WHERE")
    + "{"
    + Optional(
        Param(
            "where",
            Comp(
                "FakeGroupGraphPatten",
                ParamList("part", Comp("TriplesBlock", TriplesTemplate)),
            ),
        )
    )
    + "}"
    + SolutionModifier
    + ValuesClause,
)
AskQuery = Comp(
    "AskQuery",
    Keyword("ASK")
    + Param("datasetClause", ZeroOrMore(DatasetClause))
    + WhereClause
    + SolutionModifier
    + ValuesClause,
)
DescribeQuery = Comp(
    "DescribeQuery",
    Keyword("DESCRIBE") + OneOrMore(ParamList("var", VarOrIri))
    | "*"
    + Param("datasetClause", ZeroOrMore(DatasetClause))
    + Optional(WhereClause)
    + SolutionModifier
    + ValuesClause,
)
Update = Forward()
Query = Prologue + SelectQuery | ConstructQuery | DescribeQuery | AskQuery
UpdateUnit = Comp("Update", Update)
QueryUnit = Query
expandUnicodeEscapes_re = re.compile(r"\\u([0-9a-f]{4}(?:[0-9a-f]{4})?)", flags=re.I)

def expandUnicodeEscapes(q):
    """
    The syntax of the SPARQL Query Language is expressed over code points in Unicode [UNICODE]. The encoding is always UTF-8 [RFC3629].
    Unicode code points may also be expressed using an \\uXXXX (U+0 to U+FFFF) or \\UXXXXXXXX syntax (for U+10000 onwards) where X is a hexadecimal digit [0-9A-F]
    """
    ...

def parseQuery(q): ...
def parseUpdate(q): ...

if __name__ == "__main__":
    DEBUG = True
