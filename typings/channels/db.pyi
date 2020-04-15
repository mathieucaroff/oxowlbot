"""
This type stub file was generated by pyright.
"""

from asgiref.sync import SyncToAsync

class DatabaseSyncToAsync(SyncToAsync):
    """
    SyncToAsync version that cleans up old database connections when it exits.
    """
    def thread_handler(self, loop, *args, **kwargs):
        ...
    


database_sync_to_async = DatabaseSyncToAsync
