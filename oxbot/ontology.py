"""
Produce the query to the ontology
"""

# pyright: strict

import types
from dataclasses import dataclass
from typing import Any, List, Literal, Tuple


@dataclass
class AllIndividualInfo:
    classList: List[str]
    leftRelationList: List[Tuple[str, str]]
    rightRelationList: List[Tuple[str, str]]


def format_sparql_query(select: str, where: List[str]) -> str:
    joinline = "\n".join

    return f"""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX me: <file:littlePony.owl#>
SELECT {select} WHERE {'{'}
{joinline(f"{line}." for line in where)}
{'}'}"""


@dataclass
class Ontology:
    onto: Any
    graph: Any

    def _get(self, entityName: str):
        return self.onto[entityName]

    def _runQuery(self, query: str):
        return list(self.graph.query(query))

    def _formatAndRunQuery(self, select: str, where: List[str]):
        return self._runQuery(format_sparql_query(select, where))

    def declareIndividual(self, individualName: str, classList: List[str]):
        firstClassName = classList[0]
        FirstClass = self._get(firstClassName)
        instance = FirstClass(individualName)
        for className in classList[1:]:
            Class = self._get(className)
            instance.is_a.append(Class)

    def declareClass(self, className: str, superClassList: List[str]):
        types.new_class("NewClassName", superClassList, kwds={"namespace": self.onto})

    def declareRelation(self, subject: str, obj: str, relation: str):
        s = self._get(subject)
        objectList = s[relation]

        assert hasattr(objectList, "append"), "Implementation surprise"

        objectList.append(obj)

    def classIndividualQuery(self, className: str):
        query = format_sparql_query(
            select="?b",
            where=[
                f"?x rdfs:subClassOf* me:{className}",
                "?b rdf:type ?x",
                "?b rdf:type owl:NamedIndividual",
            ],
        )

        return self._runQuery(query)

    def relationIndividualQuery(
        self,
        individualName: str,
        relationList: str,
        mode: Literal["outward", "inward"] = "outward",
    ):
        """
        Given an individual name, and a list of relation return the list
        of individuals X who relate following the relation list transitively:

        outward mode:
        individualName -> relationList[0] -> ... -> relationList[n] -> X

        inward mode:
        X -> relationList[0] -> ... -> relationList[n] -> individualName
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        letterList = [f"?{letter}" for letter in alphabet[: len(relationList)]]

        if mode == "outward":
            left = [f"me:{individualName}"] + letterList[:-1]
            right = letterList

            select = letterList[-1]
        else:
            select = letterList[0]

            left = letterList
            right = letterList[1 : len(relationList)] + [f"me:{individualName}"]

        where = [f"{a} {r} {b}" for a, r, b in zip(left, relationList, right)]

        query = format_sparql_query(select=select, where=where)

        return self._runQuery(query)

    def allIndividualInfoQuery(self, individualName: str) -> AllIndividualInfo:
        return AllIndividualInfo(
            classList=self._formatAndRunQuery(
                select="?class", where=[f"me:{individualName} rdf:type ?class"],
            ),
            leftRelationList=self._formatAndRunQuery(
                select="?rel ?obj", where=[f"me:{individualName} ?rel ?obj"],
            ),
            rightRelationList=self._formatAndRunQuery(
                select="?rel ?obj", where=[f"?obj ?rel me:{individualName}"],
            ),
        )
