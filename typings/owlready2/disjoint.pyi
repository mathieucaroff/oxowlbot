"""
This type stub file was generated by pyright.
"""

from owlready2.namespace import *
from owlready2.entity import *
from owlready2.prop import *
from typing import Any, Optional

class AllDisjoint(object):
  def __init__(self, entities, ontology: Optional[Any] = ..., bnode: Optional[Any] = ...):
    self.ontology = ...
  
  def __getattr__(self, attr):
    ...
  
  def _callback(self, old):
    ...
  
  def _destroy_triples(self):
    ...
  
  def destroy(self):
    ...
  
  def _create_triples(self):
    ...
  
  def __repr__(self):
    ...
  


AllDifferent = AllDisjoint
def partition(mother, children):
  ...

