"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Any, Optional

class EventResultOrError:
    """
    This class wrappers the Event asyncio lock allowing either awake the
    locked Tasks without any error or raising an exception.

    thanks to @vorpalsmith for the simple design.
    """
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        ...
    
    def set(self, exc: Optional[BaseException] = ...) -> None:
        ...
    
    async def wait(self) -> Any:
        ...
    
    def cancel(self) -> None:
        """ Cancel all waiters """
        ...
    


