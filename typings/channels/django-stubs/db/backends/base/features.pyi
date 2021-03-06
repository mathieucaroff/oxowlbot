"""
This type stub file was generated by pyright.
"""

from django.db.backends.base.base import BaseDatabaseWrapper

class BaseDatabaseFeatures:
    def __init__(self, connection: BaseDatabaseWrapper) -> None:
        ...
    
    def supports_explaining_query_execution(self) -> bool:
        ...
    
    def supports_transactions(self):
        ...
    
    def supports_stddev(self):
        ...
    


