"""
This type stub file was generated by pyright.
"""

import asyncio
import datetime
import enum
from concurrent.futures import Executor
from http.cookies import SimpleCookie
from typing import Any, Iterator, Mapping, MutableMapping, Optional, TYPE_CHECKING, Tuple, Union
from multidict import CIMultiDict, istr
from .abc import AbstractStreamWriter
from .helpers import HeadersMixin
from .payload import Payload
from .typedefs import JSONEncoder, LooseHeaders
from .web_request import BaseRequest

__all__ = ('ContentCoding', 'StreamResponse', 'Response', 'json_response')
if TYPE_CHECKING:
    BaseClass = MutableMapping[str, Any]
else:
    ...
class ContentCoding(enum.Enum):
    deflate = ...
    gzip = ...
    identity = ...


class StreamResponse(BaseClass, HeadersMixin):
    _length_check = ...
    def __init__(self, *, status: int = ..., reason: Optional[str] = ..., headers: Optional[LooseHeaders] = ...) -> None:
        ...
    
    @property
    def prepared(self) -> bool:
        ...
    
    @property
    def task(self) -> asyncio.Task[None]:
        ...
    
    @property
    def status(self) -> int:
        ...
    
    @property
    def chunked(self) -> bool:
        ...
    
    @property
    def compression(self) -> bool:
        ...
    
    @property
    def reason(self) -> str:
        ...
    
    def set_status(self, status: int, reason: Optional[str] = ..., _RESPONSES: Mapping[int, Tuple[str, str]] = ...) -> None:
        ...
    
    @property
    def keep_alive(self) -> Optional[bool]:
        ...
    
    def force_close(self) -> None:
        ...
    
    @property
    def body_length(self) -> int:
        ...
    
    @property
    def output_length(self) -> int:
        ...
    
    def enable_chunked_encoding(self, chunk_size: Optional[int] = ...) -> None:
        """Enables automatic chunked transfer encoding."""
        ...
    
    def enable_compression(self, force: Optional[Union[bool, ContentCoding]] = ...) -> None:
        """Enables response compression encoding."""
        ...
    
    @property
    def headers(self) -> CIMultiDict[str]:
        ...
    
    @property
    def cookies(self) -> SimpleCookie:
        ...
    
    def set_cookie(self, name: str, value: str, *, expires: Optional[str] = ..., domain: Optional[str] = ..., max_age: Optional[Union[int, str]] = ..., path: str = ..., secure: Optional[str] = ..., httponly: Optional[str] = ..., version: Optional[str] = ...) -> None:
        """Set or update response cookie.

        Sets new cookie or updates existent with new value.
        Also updates only those params which are not None.
        """
        ...
    
    def del_cookie(self, name: str, *, domain: Optional[str] = ..., path: str = ...) -> None:
        """Delete cookie.

        Creates new empty expired cookie.
        """
        ...
    
    @property
    def content_length(self) -> Optional[int]:
        ...
    
    @content_length.setter
    def content_length(self, value: Optional[int]) -> None:
        ...
    
    @property
    def content_type(self) -> str:
        ...
    
    @content_type.setter
    def content_type(self, value: str) -> None:
        ...
    
    @property
    def charset(self) -> Optional[str]:
        ...
    
    @charset.setter
    def charset(self, value: Optional[str]) -> None:
        ...
    
    @property
    def last_modified(self) -> Optional[datetime.datetime]:
        """The value of Last-Modified HTTP header, or None.

        This header is represented as a `datetime` object.
        """
        ...
    
    @last_modified.setter
    def last_modified(self, value: Optional[Union[int, float, datetime.datetime, str]]) -> None:
        ...
    
    def _generate_content_type_header(self, CONTENT_TYPE: istr = ...) -> None:
        ...
    
    async def _do_start_compression(self, coding: ContentCoding) -> None:
        ...
    
    async def _start_compression(self, request: BaseRequest) -> None:
        ...
    
    async def prepare(self, request: BaseRequest) -> Optional[AbstractStreamWriter]:
        ...
    
    async def _start(self, request: BaseRequest) -> AbstractStreamWriter:
        ...
    
    async def write(self, data: bytes) -> None:
        ...
    
    async def drain(self) -> None:
        ...
    
    async def write_eof(self, data: bytes = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __getitem__(self, key: str) -> Any:
        ...
    
    def __setitem__(self, key: str, value: Any) -> None:
        ...
    
    def __delitem__(self, key: str) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __eq__(self, other: object) -> bool:
        ...
    


class Response(StreamResponse):
    def __init__(self, *, body: Any = ..., status: int = ..., reason: Optional[str] = ..., text: Optional[str] = ..., headers: Optional[LooseHeaders] = ..., content_type: Optional[str] = ..., charset: Optional[str] = ..., zlib_executor_size: Optional[int] = ..., zlib_executor: Executor = ...) -> None:
        ...
    
    @property
    def body(self) -> Optional[Union[bytes, Payload]]:
        ...
    
    @body.setter
    def body(self, body: bytes, CONTENT_TYPE: istr = ..., CONTENT_LENGTH: istr = ...) -> None:
        ...
    
    @property
    def text(self) -> Optional[str]:
        ...
    
    @text.setter
    def text(self, text: str) -> None:
        ...
    
    @property
    def content_length(self) -> Optional[int]:
        ...
    
    @content_length.setter
    def content_length(self, value: Optional[int]) -> None:
        ...
    
    async def write_eof(self, data: bytes = ...) -> None:
        ...
    
    async def _start(self, request: BaseRequest) -> AbstractStreamWriter:
        ...
    
    def _compress_body(self, zlib_mode: int) -> None:
        ...
    
    async def _do_start_compression(self, coding: ContentCoding) -> None:
        ...
    


def json_response(data: Any = ..., *, text: str = ..., body: bytes = ..., status: int = ..., reason: Optional[str] = ..., headers: LooseHeaders = ..., content_type: str = ..., dumps: JSONEncoder = ...) -> Response:
    ...

