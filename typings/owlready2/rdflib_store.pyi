"""
This type stub file was generated by pyright.
"""

import rdflib
from owlready2.base import *
from typing import Any, Optional

class TripleLiteRDFlibStore(rdflib.store.Store):
  context_aware = ...
  def __init__(self, world):
    self.world = ...
    self.triplelite = ...
    self.main_graph = ...
    self.context_graphs = ...
  
  def _2_python(self, x):
    ...
  
  def _rdflib_2_owlready(self, spo):
    ...
  
  def _owlready_2_rdflib(self, s, p, o, d: Optional[Any] = ...):
    ...
  
  def add(self, xxx_todo_changeme, context, quoted: bool = ...):
    ...
  
  def remove(self, xxx_todo_changeme, context: Optional[Any] = ...):
    ...
  
  def triples(self, triple_pattern, context: Optional[Any] = ...):
    ...
  
  def __len__(self, context: Optional[Any] = ...):
    ...
  
  def contexts(self, triple: Optional[Any] = ...):
    ...
  
  def bind(self, prefix, namespace):
    ...
  
  def namespace(self, prefix):
    ...
  
  def prefix(self, namespace):
    ...
  
  def namespaces(self):
    ...
  
  def get_context(self, identifier_or_ontology):
    ...
  


class TripleLiteRDFlibGraph(rdflib.Graph):
  def query_owlready(self, query, *args, **kargs):
    ...
  
  def _rdflib_2_owlready(self, o):
    ...
  
  def get_context(self, onto):
    ...
  
  def BNode(self):
    ...
  


