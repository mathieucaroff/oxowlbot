"""
This type stub file was generated by pyright.
"""

from owlready2.base import *
from owlready2.namespace import *
from owlready2.individual import *
from owlready2.prop import *
from typing import Any, Optional

swrl = owl_world.get_ontology("http://www.w3.org/2003/11/swrl#")
class Variable(Thing):
  namespace = ...
  def __str__(self):
    ...
  
  def __repr__(self):
    ...
  
  def __init__(self, name: Optional[Any] = ..., namespace: Optional[Any] = ..., **kargs):
    ...
  


class body(ObjectProperty):
  namespace = ...


class head(ObjectProperty):
  namespace = ...


class classPredicate(ObjectProperty, FunctionalProperty):
  namespace = ...


class propertyPredicate(ObjectProperty, FunctionalProperty):
  namespace = ...


class arguments(ObjectProperty):
  namespace = ...


class builtin(ObjectProperty, FunctionalProperty):
  namespace = ...


_DATARANGES = { int: "int",float: "decimal",str: "string",normstr: "normalizedString" }
_NAME_2_DATARANGE = { v: k for (k, v) in _DATARANGES.items() }
class Imp(Thing):
  namespace = ...
  def __str__(self):
    ...
  
  def __repr__(self):
    ...
  
  def __init__(self, name=..., namespace: Optional[Any] = ..., **kargs):
    ...
  
  def __getattr__(self, attr):
    ...
  
  def get_variable(self, name, create: bool = ...):
    ...
  
  def set_as_rule(self, rule, namespaces: Optional[Any] = ...):
    ...
  
  def __destroy__(self, objs, datas):
    ...
  


def _find_entity(name, namespaces):
  ...

class _FixedArguments(object):
  def __init__(self, name=..., namespace: Optional[Any] = ..., **kargs):
    ...
  
  def __str__(self):
    ...
  
  def __getattr__(self, attr):
    ...
  
  def __destroy__(self):
    ...
  


class ClassAtom(_FixedArguments, Thing):
  namespace = ...
  def __repr__(self):
    ...
  


class DataRangeAtom(_FixedArguments, Thing):
  namespace = ...
  def __repr__(self):
    ...
  
  def __getattr__(self, attr):
    ...
  
  def __setattr__(self, attr, value):
    ...
  


class SameIndividualAtom(_FixedArguments, Thing):
  namespace = ...
  def __repr__(self):
    ...
  


class DifferentIndividualsAtom(_FixedArguments, Thing):
  namespace = ...
  def __repr__(self):
    ...
  


class DatavaluedPropertyAtom(_FixedArguments, Thing):
  namespace = ...
  def __init__(self, name=..., namespace: Optional[Any] = ..., **kargs):
    ...
  
  def __repr__(self):
    ...
  


class IndividualPropertyAtom(_FixedArguments, Thing):
  namespace = ...
  def __init__(self, name=..., namespace: Optional[Any] = ..., **kargs):
    ...
  
  def __repr__(self):
    ...
  


_BUILTINS = "equal", "notEqual", "lessThan", "lessThanOrEqual", "greaterThan", "greaterThanOrEqual", "add", "subtract", "multiply", "divide", "integerDivide", "mod", "pow", "unaryPlus", "unaryMinus", "abs", "ceiling", "floor", "round", "roundHalfToEven", "sin", "cos", "tan", "booleanNot", "stringEqualIgnoreCase", "stringConcat", "substring", "stringLength", "normalizeSpace", "upperCase", "lowerCase", "translate", "contains", "containsIgnoreCase", "startsWith", "endsWith", "substringBefore", "substringAfter", "matches", "replace", "tokenize", "yearMonthDuration", "dayTimeDuration", "dateTime", "date", "time", "addYearMonthDurations", "subtractYearMonthDurations", "multiplyYearMonthDuration", "divideYearMonthDurations", "addDayTimeDurations", "subtractDayTimeDurations", "multiplyDayTimeDurations", "divideDayTimeDuration", "subtractDates", "subtractTimes", "addYearMonthDurationToDateTime", "addDayTimeDurationToDateTime", "subtractYearMonthDurationFromDateTime", "subtractDayTimeDurationFromDateTime", "addYearMonthDurationToDate", "addDayTimeDurationToDate", "subtractYearMonthDurationFromDate", "subtractDayTimeDurationFromDate", "addDayTimeDurationToTime", "subtractDayTimeDurationFromTime", "subtractDateTimesYieldingYearMonthDuration", "subtractDateTimesYieldingDayTimeDuration", "resolveURI", "anyURI", "listConcat", "listIntersection", "listSubtraction", "member", "length", "first", "rest", "sublist", "empty"
class BuiltinAtom(Thing):
  namespace = ...
  def __init__(self, name=..., namespace: Optional[Any] = ..., **kargs):
    ...
  
  def __str__(self):
    ...
  
  def __repr__(self):
    ...
  
  def __getattr__(self, attr):
    ...
  
  def __setattr__(self, attr, value):
    ...
  
  def __destroy__(self):
    ...
  


class OrderedValueList(CallbackList):
  __slots__ = ...
  def __init__(self, bn, obj, Prop):
    ...
  
  def _callback(self, obj, old):
    ...
  


class ArgumentValueList(CallbackList):
  __slots__ = ...
  def __init__(self, obj):
    ...
  
  def _callback(self, obj, old):
    ...
  


def _repr_swrl(x):
  ...

_RULE_PARSER = None
def _create_rule_parser():
  ...

