
from owlready2 import get_ontology, default_world

onto = get_ontology("owl/littlePony.owl")
onto.load()
graph = default_world.as_rdflib_graph()

entity = onto.Sphinx

print(entity)
