"""
This type stub file was generated by pyright.
"""

import owlready2.namespace
import owlready2.entity
import owlready2.prop
import owlready2.class_construct
import owlready2.triplelite
from owlready2.base import *
from owlready2.namespace import *
from owlready2.entity import *
from owlready2.prop import *
from owlready2.prop import _FUNCTIONAL_FOR_CACHE
from owlready2.individual import *
from owlready2.class_construct import *
from owlready2.disjoint import *
from owlready2.annotation import *
from owlready2.reasoning import *
from owlready2.reasoning import _keep_most_specific
from owlready2.close import *
from owlready2.rule import *

VERSION = "0.23"
JAVA_EXE = "java"
default_wordl: World
default_world = IRIS = World()
get_ontology = default_world.get_ontology
get_namespace = default_world.get_namespace

def default_render_func(entity): ...
def set_render_func(func): ...
