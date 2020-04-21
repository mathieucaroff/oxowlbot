from owlready2 import *
from rdflib import *
import rdflib.plugins.sparql as sparql
import re

onto = get_ontology("owl/wildlife.owl").load()
# default_world.graph.dump()

graph = default_world.as_rdflib_graph()

def build_SPARQL_query(id,classe):
    if (id==1):
        return """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX me: <file:wildlife.owl#>
SELECT ?b WHERE {
?x rdfs:subClassOf* me:%s .
?b rdf:type ?x .
?b rdf:type owl:NamedIndividual .
}""" % classe

re_gir=re.compile(r'giraffe')
re_ant=re.compile(r'antilope')

def strip_namespace(x):
    return re.sub(r'^[^#]*#',"",str(x))

ext_genre={}
ext_genre["lion"]=""
ext_genre["giraffe"]="e"

def gender_of(x):
    global ext_genre
    if (x in ext_genre.keys()):
        return ext_genre[x]
    else:
        return ""

def format_plusieurs(resultat):
    if (len(resultat)==0):
        return ""
    elif (len(resultat)==1):
        return resultat[0]
    elif (len(resultat)>1):
        return ", ".join(resultat[:len(resultat)-1])+" et "+resultat[-1]


resultat = []

lemme = "giraffe"

query = sparql.prepareQuery(build_SPARQL_query(1,lemme))
qres = graph.query(query)

for q in qres:
    resultat.append(str(q[0]))
if (len(resultat)==0):
    print("Il n'y a aucun%s %s." % (gender_of(lemme), lemme))
elif (len(resultat)==1):
    print("Il y a un%s seul%s %s. C'est %s." % (gender_of(lemme), gender_of(lemme), lemme, resultat[0]))
else:
    print("Il y a %i %ss. Ce sont %s." % (len(resultat), lemme, format_plusieurs(resultat)))
