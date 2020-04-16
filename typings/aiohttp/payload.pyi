"""
This type stub file was generated by pyright.
"""

import enum
from abc import ABC, abstractmethod
from typing import Any, AsyncIterable, AsyncIterator, ByteString, Dict, IO, Iterable, Optional, TYPE_CHECKING, Text, TextIO, Tuple, Type, Union
from .abc import AbstractStreamWriter
from .streams import StreamReader
from .typedefs import JSONEncoder, _CIMultiDict

__all__ = ('PAYLOAD_REGISTRY', 'get_payload', 'payload_type', 'Payload', 'BytesPayload', 'StringPayload', 'IOBasePayload', 'BytesIOPayload', 'BufferedReaderPayload', 'TextIOPayload', 'StringIOPayload', 'JsonPayload', 'AsyncIterablePayload')
TOO_LARGE_BYTES_BODY = 2 ** 20
if TYPE_CHECKING:
    ...
class LookupError(Exception):
    ...


class Order(str, enum.Enum):
    normal = ...
    try_first = ...
    try_last = ...


def get_payload(data: Any, *args: Any, **kwargs: Any) -> Payload:
    ...

def register_payload(factory: Type[Payload], type: Any, *, order: Order = ...) -> None:
    ...

class payload_type:
    def __init__(self, type: Any, *, order: Order = ...) -> None:
        self.type = ...
        self.order = ...
    
    def __call__(self, factory: Type[Payload]) -> Type[Payload]:
        ...
    


class PayloadRegistry:
    """Payload registry.

    note: we need zope.interface for more efficient adapter search
    """
    def __init__(self) -> None:
        ...
    
    def get(self, data: Any, *args: Any, _CHAIN: Any = ..., **kwargs: Any) -> Payload:
        ...
    
    def register(self, factory: Type[Payload], type: Any, *, order: Order = ...) -> None:
        ...
    


class Payload(ABC):
    _default_content_type = ...
    _size = ...
    def __init__(self, value: Any, headers: Optional[Union[_CIMultiDict, Dict[str, str], Iterable[Tuple[str, str]]]] = ..., content_type: Optional[str] = ..., filename: Optional[str] = ..., encoding: Optional[str] = ..., **kwargs: Any) -> None:
        ...
    
    @property
    def size(self) -> Optional[int]:
        """Size of the payload."""
        ...
    
    @property
    def filename(self) -> Optional[str]:
        """Filename of the payload."""
        ...
    
    @property
    def headers(self) -> _CIMultiDict:
        """Custom item headers"""
        ...
    
    @property
    def _binary_headers(self) -> bytes:
        ...
    
    @property
    def encoding(self) -> Optional[str]:
        """Payload encoding"""
        ...
    
    @property
    def content_type(self) -> str:
        """Content type"""
        ...
    
    def set_content_disposition(self, disptype: str, quote_fields: bool = ..., **params: Any) -> None:
        """Sets ``Content-Disposition`` header."""
        ...
    
    @abstractmethod
    async def write(self, writer: AbstractStreamWriter) -> None:
        """Write payload.

        writer is an AbstractStreamWriter instance:
        """
        ...
    


class BytesPayload(Payload):
    def __init__(self, value: ByteString, *args: Any, **kwargs: Any) -> None:
        ...
    
    async def write(self, writer: AbstractStreamWriter) -> None:
        ...
    


class StringPayload(BytesPayload):
    def __init__(self, value: Text, *args: Any, encoding: Optional[str] = ..., content_type: Optional[str] = ..., **kwargs: Any) -> None:
        ...
    


class StringIOPayload(StringPayload):
    def __init__(self, value: IO[str], *args: Any, **kwargs: Any) -> None:
        ...
    


class IOBasePayload(Payload):
    def __init__(self, value: IO[Any], disposition: str = ..., *args: Any, **kwargs: Any) -> None:
        ...
    
    async def write(self, writer: AbstractStreamWriter) -> None:
        ...
    


class TextIOPayload(IOBasePayload):
    def __init__(self, value: TextIO, *args: Any, encoding: Optional[str] = ..., content_type: Optional[str] = ..., **kwargs: Any) -> None:
        ...
    
    @property
    def size(self) -> Optional[int]:
        ...
    
    async def write(self, writer: AbstractStreamWriter) -> None:
        ...
    


class BytesIOPayload(IOBasePayload):
    @property
    def size(self) -> int:
        ...
    


class BufferedReaderPayload(IOBasePayload):
    @property
    def size(self) -> Optional[int]:
        ...
    


class JsonPayload(BytesPayload):
    def __init__(self, value: Any, encoding: str = ..., content_type: str = ..., dumps: JSONEncoder = ..., *args: Any, **kwargs: Any) -> None:
        ...
    


if TYPE_CHECKING:
    _AsyncIterator = AsyncIterator[bytes]
    _AsyncIterable = AsyncIterable[bytes]
else:
    ...
class AsyncIterablePayload(Payload):
    _iter = ...
    def __init__(self, value: _AsyncIterable, *args: Any, **kwargs: Any) -> None:
        ...
    
    async def write(self, writer: AbstractStreamWriter) -> None:
        ...
    


class StreamReaderPayload(AsyncIterablePayload):
    def __init__(self, value: StreamReader, *args: Any, **kwargs: Any) -> None:
        ...
    


PAYLOAD_REGISTRY = PayloadRegistry()
