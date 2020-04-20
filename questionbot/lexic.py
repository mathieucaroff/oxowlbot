# pyright: strict

import logging

from .util.flatten import flatten
from typing import Dict, List, Tuple
from . import ontology as o


def normalize(name: str) -> str:
    return name.lower().replace(' ', '_')

def listDesignation(individualNameList: List[str]):
    return [
        designationPair
        for name in individualNameList
        for designationPair in listDesignationForOneName(name)
    ]


def listDesignationForOneName(individualName: str) -> List[Tuple[bool, str]]:
    """
    Produce a list of individual designations associated with the individual name.
    The list of results also contains a boolean, to indicate when a designation
    is exact, and thus should receive special treatment.
    """
    nameList = normalize(individualName).split('_')

    designationList: List[Tuple[bool, str]] = []

    for kl in range(0, len(nameList)):
        for kr in range(kl + 1, len(nameList) + 1):
            designation = " ".join(nameList[kl:kr])
            designationList.append((False, designation))

    designationList.sort(key=lambda pair: len(pair[1]))

    _, fullName = designationList[-1]
    designationList[-1] = (True, fullName)

    assert all(type(a) == bool and type(b) == str for a, b in designationList)  # type: ignore

    return designationList


class Lexic:
    individualTable: Dict[str, List[str]]
    relationTable: Dict[str, str]
    classTable: Dict[str, str]

    def __init__(self, ontology: o.Ontology):
        self.ontology = ontology
        self.individualTable = {}
        self.relationTable = {}
        self.classTable = {}
        self._fill()

    def getIndividualList(self, name: str) -> List[str]:
        return self.individualTable[normalize(name)]

    def getRelation(self, name: str) -> str:
        return self.relationTable[normalize(name)]

    def getClass(self, name: str) -> str:
        return self.classTable[normalize(name)]

    def _fill(self):

        # Individual
        individualList = self.ontology.formatAndRunQuery(
            select="?individual", where=["?individual rdf:type owl:NamedIndividual"],
        )
        for (individualName,) in individualList:
            individual = self.ontology.get(individualName)
            if individual is None:
                logging.error('broken assertion: missing individual -- ignored')
                continue

            if individual.alias is not None:
                pass
            for priority, individualDesignation in listDesignationForOneName(
                individualName
            ):
                entry = self.individualTable.setdefault(individualDesignation, [])
                if priority:
                    entry.insert(0, individualName)
                else:
                    entry.append(individualName)

        # Class
        classList = self.ontology.formatAndRunQuery(
            select="?class", where=["?class rdf:type rdfs:Class"],
        )
        for (className,) in classList:
            classDesignation = normalize(className)
            self.classTable[classDesignation] = className

        # Relation
        relationList = flatten(self.ontology.formatAndRunQuery(
            select="?relation",
            where=["?relation rdf:type owl:ObjectProperty"],
        ))
        for relationName in relationList:
            relationDesignation = normalize(relationName.split("_")[0])
            self.relationTable[relationDesignation] = relationName

