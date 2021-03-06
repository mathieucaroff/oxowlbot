"""
This type stub file was generated by pyright.
"""

from typing import Any, ContextManager, List, Optional, Sequence, Tuple, Type, Union
from django.db.backends.ddl_references import Statement
from django.db.models.base import Model
from django.db.models.indexes import Index
from django.db.models.fields import Field

logger: Any
class BaseDatabaseSchemaEditor(ContextManager[Any]):
    def __init__(self, connection: Any, collect_sql: bool = ..., atomic: bool = ...) -> None:
        ...
    
    def __enter__(self) -> BaseDatabaseSchemaEditor:
        ...
    
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        ...
    
    def execute(self, sql: Union[Statement, str], params: Optional[Union[List[int], Tuple]] = ...) -> None:
        ...
    
    def quote_name(self, name: str) -> str:
        ...
    
    def column_sql(self, model: Type[Model], field: Field, include_default: bool = ...) -> Tuple[Optional[str], Optional[List[Any]]]:
        ...
    
    def skip_default(self, field: Any):
        ...
    
    def prepare_default(self, value: Any) -> None:
        ...
    
    def effective_default(self, field: Field) -> Optional[Union[int, str]]:
        ...
    
    def quote_value(self, value: Any) -> None:
        ...
    
    def create_model(self, model: Type[Model]) -> None:
        ...
    
    def delete_model(self, model: Type[Model]) -> None:
        ...
    
    def add_index(self, model: Type[Model], index: Index) -> None:
        ...
    
    def remove_index(self, model: Type[Model], index: Index) -> None:
        ...
    
    def alter_unique_together(self, model: Type[Model], old_unique_together: Sequence[Sequence[str]], new_unique_together: Sequence[Sequence[str]]) -> None:
        ...
    
    def alter_index_together(self, model: Type[Model], old_index_together: Sequence[Sequence[str]], new_index_together: Sequence[Sequence[str]]) -> None:
        ...
    
    def alter_db_table(self, model: Type[Model], old_db_table: str, new_db_table: str) -> None:
        ...
    
    def alter_db_tablespace(self, model: Any, old_db_tablespace: Any, new_db_tablespace: Any) -> None:
        ...
    
    def add_field(self, model: Any, field: Any):
        ...
    
    def remove_field(self, model: Any, field: Any):
        ...
    
    def alter_field(self, model: Type[Model], old_field: Field, new_field: Field, strict: bool = ...) -> None:
        ...
    
    def remove_procedure(self, procedure_name: Any, param_types: Any = ...) -> None:
        ...
    


