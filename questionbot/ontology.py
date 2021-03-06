"""
Produce the query to the ontology
"""

# pyright: strict

import dataclasses as dc
import logging
import types
from typing import Any, List, Literal, Tuple

from .queryLogger import QueryLogger
from .util.flatten import flatten
from .util.tuple import tuple2

x = [0]

QUERY_TEMPLATE = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX me: <{me}>
SELECT {select} WHERE {{
{whereBloc}
}}"""


@dc.dataclass
class IndividualInfo:
    relationList: List[Tuple[str, str]]

    def asdict(self):
        return dc.asdict(self)


@dc.dataclass
class Ontology:
    onto: Any
    queryLogger: QueryLogger

    def get(self, entityName: str):
        return self.onto[entityName]

    def _runQuery(self, query: str) -> List[List[str]]:
        result = []
        graph = self.onto.world.as_rdflib_graph()
        for row in graph.query(query):
            result.append([self._namePart(elem) for elem in row])
        return result

    def _namePart(self, elem: Any) -> str:
        if '#' not in elem:
            logging.error(elem)
            breakpoint()
            return ''
        _, name = elem.split("#")
        return name

    def _formatSparqlQuery(self, select: str, where: List[str]) -> str:
        whereBloc = "\n".join(f"{line}." for line in where)

        result = QUERY_TEMPLATE.format(
            me=self.onto.base_iri, select=select, whereBloc=whereBloc,
        )

        return result

    def formatAndRunQuery(
        self,
        select: str,
        where: List[str],
        set_breakpoint: bool = False,
        log: bool = True,
    ):
        fullQuery = self._formatSparqlQuery(select, where)
        if set_breakpoint:
            breakpoint()
        result = self._runQuery(fullQuery)
        if log:
            self.queryLogger.write(select, where, fullQuery, result)
        return result

    def declareIndividual(self, individualName: str, classList: List[str]):
        firstClassName = classList[0]
        FirstClass = self.get(firstClassName)
        instance = FirstClass(individualName)
        for className in classList[1:]:
            Class = self.get(className)
            instance.is_a.append(Class)

    def declareClass(self, className: str, superClassList: List[str]):
        types.new_class(
            "NewClassName", superClassList, kwds={"namespace": self.onto}
        )

    def declareRelation(self, subject: str, obj: str, relation: str):
        s = self.get(subject)
        objectList = s[relation]

        assert hasattr(objectList, "append"), "Implementation surprise"

        objectList.append(obj)

    def allIndividual(self):
        return self.onto.individuals()

    def classIndividualQuery(self, classList: List[str]):
        where = [f"?b rdf:type me:{className}" for className in classList]

        result = flatten(self.formatAndRunQuery(select="?b", where=where))

        return result

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

        where = [f"{a} me:{r} {b}" for a, r, b in zip(left, relationList, right)]

        return flatten(self.formatAndRunQuery(select=select, where=where))

    def individualInfoQuery(self, individualName: str) -> IndividualInfo:
        rawRelationList = tuple2(
            self.formatAndRunQuery(
                select="?rel ?obj", where=[f"me:{individualName} ?rel ?obj"],
            )
        )

        relationList = [
            (rel, target)
            for rel, target in rawRelationList
            if target != "NamedIndividual"
        ]

        info = IndividualInfo(relationList=relationList,)
        return info
