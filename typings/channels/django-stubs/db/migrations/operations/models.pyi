"""
This type stub file was generated by pyright.
"""

from typing import Any, Collection, Dict, List, Optional, Sequence, Tuple, Union
from django.db.migrations.operations.base import Operation
from django.db.models.indexes import Index
from django.db.models.manager import Manager
from django.db.models.constraints import BaseConstraint
from django.db.models.fields import Field

class ModelOperation(Operation):
    def __init__(self, name: str) -> None:
        ...
    
    def name_lower(self) -> str:
        ...
    


class CreateModel(ModelOperation):
    def __init__(self, name: str, fields: Sequence[Tuple[str, Field]], options: Optional[Dict[str, Any]] = ..., bases: Optional[Sequence[Union[type, str]]] = ..., managers: Optional[Sequence[Tuple[str, Manager]]] = ...) -> None:
        ...
    
    def model_to_key(self, model: str) -> List[str]:
        ...
    


class DeleteModel(ModelOperation):
    ...


class RenameModel(ModelOperation):
    def __init__(self, old_name: str, new_name: str) -> None:
        ...
    
    def old_name_lower(self) -> str:
        ...
    
    def new_name_lower(self) -> str:
        ...
    


class AlterModelTable(ModelOperation):
    def __init__(self, name: str, table: Optional[str]) -> None:
        ...
    


class ModelOptionOperation(ModelOperation):
    ...


class FieldRelatedOptionOperation(ModelOptionOperation):
    ...


class AlterUniqueTogether(FieldRelatedOptionOperation):
    def __init__(self, name: str, unique_together: Optional[Collection[Sequence[str]]]) -> None:
        ...
    


class AlterIndexTogether(FieldRelatedOptionOperation):
    def __init__(self, name: str, index_together: Optional[Collection[Sequence[str]]]) -> None:
        ...
    


class AlterOrderWithRespectTo(FieldRelatedOptionOperation):
    def __init__(self, name: str, order_with_respect_to: str) -> None:
        ...
    


class AlterModelOptions(ModelOptionOperation):
    def __init__(self, name: str, options: Dict[str, Any]) -> None:
        ...
    


class AlterModelManagers(ModelOptionOperation):
    def __init__(self, name: Any, managers: Any) -> None:
        ...
    


class IndexOperation(Operation):
    def model_name_lower(self):
        ...
    


class AddIndex(IndexOperation):
    def __init__(self, model_name: str, index: Union[str, Index]) -> None:
        ...
    


class RemoveIndex(IndexOperation):
    def __init__(self, model_name: str, name: Union[str, Index]) -> None:
        ...
    


class AddConstraint(IndexOperation):
    def __init__(self, model_name: str, constraint: BaseConstraint):
        ...
    


class RemoveConstraint(IndexOperation):
    def __init__(self, model_name: str, name: str) -> None:
        ...
    


