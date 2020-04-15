"""
This type stub file was generated by pyright.
"""

from asgiref.testing import ApplicationCommunicator
from typing import Any, Optional

class HttpCommunicator(ApplicationCommunicator):
    """
    ApplicationCommunicator subclass that has HTTP shortcut methods.

    It will construct the scope for you, so you need to pass the application
    (uninstantiated) along with HTTP parameters.

    This does not support full chunking - for that, just use ApplicationCommunicator
    directly.
    """
    def __init__(self, application, method, path, body=..., headers: Optional[Any] = ...):
        self.scope = ...
        self.body = ...
        self.sent_request = ...
    
    async def get_response(self, timeout=...):
        """
        Get the application's response. Returns a dict with keys of
        "body", "headers" and "status".
        """
        ...
    


