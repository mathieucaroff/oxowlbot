"""
This type stub file was generated by pyright.
"""

from . import operators, parser, parserutils
from .processor import prepareQuery, processUpdate

"""
SPARQL implementation for RDFLib

.. versionadded:: 4.0
"""
SPARQL_LOAD_GRAPHS = True
SPARQL_DEFAULT_GRAPH_UNION = True
CUSTOM_EVALS = {  }
PLUGIN_ENTRY_POINT = 'rdf.plugins.sparqleval'
