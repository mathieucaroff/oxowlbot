"""
This type stub file was generated by pyright.
"""

from owlready2.base import *
from owlready2.namespace import *
from typing import Any, Optional

class _EquivalentToList(CallbackList):
  __slots__ = ...
  def __init__(self, l, obj, callback):
    ...
  
  def _build_indirect(self):
    ...
  
  def indirect(self):
    ...
  
  def self_and_indirect_equivalent(self):
    ...
  


class _DisjointUnionList(CallbackList):
  __slots__ = ...
  def __init__(self, l, obj, bn):
    ...
  
  def callback(self, obj, old):
    ...
  


class EntityClass(type):
  namespace = ...
  def get_name(Class):
    ...
  
  def set_name(Class, name):
    ...
  
  name = ...
  def get_iri(Class):
    ...
  
  def set_iri(Class, new_iri):
    ...
  
  iri = ...
  _owl_type = ...
  _rdfs_is_a = ...
  _owl_equivalent = ...
  _owl_disjointwith = ...
  _owl_alldisjoint = ...
  @staticmethod
  def _find_base_classes(is_a):
    ...
  
  def mro(Class):
    ...
  
  def __new__(MetaClass, name, superclasses, obj_dict):
    ...
  
  def _add_is_a_triple(Class, base):
    ...
  
  def _del_is_a_triple(Class, base):
    ...
  
  def __init__(Class, name, bases, obj_dict):
    ...
  
  def get_equivalent_to(Class):
    ...
  
  def set_equivalent_to(Class, value):
    ...
  
  equivalent_to = ...
  def get_indirect_equivalent_to(Class):
    ...
  
  INDIRECT_equivalent_to = ...
  def _class_equivalent_to_changed(Class, old):
    ...
  
  def __setattr__(Class, attr, value):
    ...
  
  def _class_is_a_changed(Class, old):
    ...
  
  def disjoints(Class):
    ...
  
  def ancestors(Class, include_self: bool = ..., include_constructs: bool = ...):
    ...
  
  def descendants(Class, include_self: bool = ..., only_loaded: bool = ..., world: Optional[Any] = ...):
    ...
  
  def _fill_ancestors(Class, s, include_self, include_constructs):
    ...
  
  def _fill_descendants(Class, s, include_self, only_loaded, world, onto):
    ...
  
  def subclasses(Class, only_loaded: bool = ..., world: Optional[Any] = ...):
    ...
  
  def constructs(Class, Prop: Optional[Any] = ...):
    ...
  


def issubclass_owlready(Class, Parent_or_tuple):
  ...

issubclass = issubclass_owlready
def isinstance_python(obj, class_or_tuple):
  ...

class ThingClass(EntityClass):
  namespace = ...
  def __instancecheck__(Class, instance):
    ...
  
  def _satisfied_by(Class, x):
    ...
  
  def _get_class_possible_relations(Class):
    ...
  
  def get_disjoint_unions(Class):
    ...
  
  def set_disjoint_unions(Class, dus):
    ...
  
  def _disjoint_union_changed(Class, old):
    ...
  
  disjoint_unions = ...
  def instances(Class, world: Optional[Any] = ...):
    ...
  
  def direct_instances(Class, world: Optional[Any] = ...):
    ...
  
  def get_class_properties(Class):
    ...
  
  def INDIRECT_get_class_properties(Class):
    ...
  
  def __and__(a, b):
    ...
  
  def __or__(a, b):
    ...
  
  def __invert__(a):
    ...
  
  def __rshift__(Domain, Range):
    ...
  
  def get_defined_class(Class):
    ...
  
  def set_defined_class(Class, defined_class):
    ...
  
  defined_class = ...
  def __getattr__(Class, attr):
    ...
  
  def __setattr__(Class, attr, value):
    ...
  
  def inverse_restrictions(Class, Prop: Optional[Any] = ...):
    ...
  
  def _get_defined_construct(Class):
    ...
  
  def _on_class_prop_changed(Class, Prop, old, new):
    ...
  


def _inherited_property_value_restrictions(x, Prop, already):
  ...
