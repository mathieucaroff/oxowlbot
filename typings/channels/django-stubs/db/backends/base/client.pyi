"""
This type stub file was generated by pyright.
"""

from django.db.backends.base.base import BaseDatabaseWrapper

class BaseDatabaseClient:
    def __init__(self, connection: BaseDatabaseWrapper) -> None:
        ...
    
    def runshell(self) -> None:
        ...
    


