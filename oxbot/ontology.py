"""
Produce the query to the ontology
"""

# pyright: strict

from typing import Any
from dataclasses import dataclass


@dataclass
class Ontology:
    graph: Any
