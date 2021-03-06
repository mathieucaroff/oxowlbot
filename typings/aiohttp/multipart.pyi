"""
This type stub file was generated by pyright.
"""

from types import TracebackType
from typing import Any, Dict, Iterator, List, Mapping, Optional, Sequence, TYPE_CHECKING, Tuple, Type, Union
from multidict import CIMultiDictProxy, MultiMapping
from .helpers import reify
from .payload import Order, Payload, payload_type
from .streams import StreamReader
from .client_reqrep import ClientResponse

__all__ = ('MultipartReader', 'MultipartWriter', 'BodyPartReader', 'BadContentDispositionHeader', 'BadContentDispositionParam', 'parse_content_disposition', 'content_disposition_filename')
if TYPE_CHECKING:
    ...
class BadContentDispositionHeader(RuntimeWarning):
    ...


class BadContentDispositionParam(RuntimeWarning):
    ...


def parse_content_disposition(header: Optional[str]) -> Tuple[Optional[str], Dict[str, str]]:
    ...

def content_disposition_filename(params: Mapping[str, str], name: str = ...) -> Optional[str]:
    ...

class MultipartResponseWrapper:
    """Wrapper around the MultipartReader.

    It takes care about
    underlying connection and close it when it needs in.
    """
    def __init__(self, resp: ClientResponse, stream: MultipartReader) -> None:
        self.resp = ...
        self.stream = ...
    
    def __aiter__(self) -> MultipartResponseWrapper:
        ...
    
    async def __anext__(self) -> Union[MultipartReader, BodyPartReader]:
        ...
    
    def at_eof(self) -> bool:
        """Returns True when all response data had been read."""
        ...
    
    async def next(self) -> Optional[Union[MultipartReader, BodyPartReader]]:
        """Emits next multipart reader object."""
        ...
    
    async def release(self) -> None:
        """Releases the connection gracefully, reading all the content
        to the void."""
        ...
    


class BodyPartReader:
    """Multipart reader for single body part."""
    chunk_size = ...
    def __init__(self, boundary: bytes, headers: CIMultiDictProxy[str], content: StreamReader) -> None:
        self.headers = ...
    
    def __aiter__(self) -> BodyPartReader:
        ...
    
    async def __anext__(self) -> bytes:
        ...
    
    async def next(self) -> Optional[bytes]:
        ...
    
    async def read(self, *, decode: bool = ...) -> bytes:
        """Reads body part data.

        decode: Decodes data following by encoding
                method from Content-Encoding header. If it missed
                data remains untouched
        """
        ...
    
    async def read_chunk(self, size: int = ...) -> bytes:
        """Reads body part content chunk of the specified size.

        size: chunk size
        """
        ...
    
    async def _read_chunk_from_length(self, size: int) -> bytes:
        ...
    
    async def _read_chunk_from_stream(self, size: int) -> bytes:
        ...
    
    async def readline(self) -> bytes:
        """Reads body part by line by line."""
        ...
    
    async def release(self) -> None:
        """Like read(), but reads all the data to the void."""
        ...
    
    async def text(self, *, encoding: Optional[str] = ...) -> str:
        """Like read(), but assumes that body part contains text data."""
        ...
    
    async def json(self, *, encoding: Optional[str] = ...) -> Optional[Dict[str, Any]]:
        """Like read(), but assumes that body parts contains JSON data."""
        ...
    
    async def form(self, *, encoding: Optional[str] = ...) -> List[Tuple[str, str]]:
        """Like read(), but assumes that body parts contains form
        urlencoded data.
        """
        ...
    
    def at_eof(self) -> bool:
        """Returns True if the boundary was reached or False otherwise."""
        ...
    
    def decode(self, data: bytes) -> bytes:
        """Decodes data according the specified Content-Encoding
        or Content-Transfer-Encoding headers value.
        """
        ...
    
    def _decode_content(self, data: bytes) -> bytes:
        ...
    
    def _decode_content_transfer(self, data: bytes) -> bytes:
        ...
    
    def get_charset(self, default: str) -> str:
        """Returns charset parameter from Content-Type header or default."""
        ...
    
    @reify
    def name(self) -> Optional[str]:
        """Returns name specified in Content-Disposition header or None
        if missed or header is malformed.
        """
        ...
    
    @reify
    def filename(self) -> Optional[str]:
        """Returns filename specified in Content-Disposition header or None
        if missed or header is malformed.
        """
        ...
    


@payload_type(BodyPartReader, order=Order.try_first)
class BodyPartReaderPayload(Payload):
    def __init__(self, value: BodyPartReader, *args: Any, **kwargs: Any) -> None:
        ...
    
    async def write(self, writer: Any) -> None:
        ...
    


class MultipartReader:
    """Multipart body reader."""
    response_wrapper_cls = ...
    multipart_reader_cls = ...
    part_reader_cls = ...
    def __init__(self, headers: Mapping[str, str], content: StreamReader) -> None:
        self.headers = ...
    
    def __aiter__(self) -> MultipartReader:
        ...
    
    async def __anext__(self) -> Union[MultipartReader, BodyPartReader]:
        ...
    
    @classmethod
    def from_response(cls, response: ClientResponse) -> MultipartResponseWrapper:
        """Constructs reader instance from HTTP response.

        :param response: :class:`~aiohttp.client.ClientResponse` instance
        """
        ...
    
    def at_eof(self) -> bool:
        """Returns True if the final boundary was reached or
        False otherwise.
        """
        ...
    
    async def next(self) -> Optional[Union[MultipartReader, BodyPartReader]]:
        """Emits the next multipart body part."""
        ...
    
    async def release(self) -> None:
        """Reads all the body parts to the void till the final boundary."""
        ...
    
    async def fetch_next_part(self) -> Union[MultipartReader, BodyPartReader]:
        """Returns the next body part reader."""
        ...
    
    def _get_part_reader(self, headers: CIMultiDictProxy[str]) -> Union[MultipartReader, BodyPartReader]:
        """Dispatches the response by the `Content-Type` header, returning
        suitable reader instance.

        :param dict headers: Response headers
        """
        ...
    
    def _get_boundary(self) -> str:
        ...
    
    async def _readline(self) -> bytes:
        ...
    
    async def _read_until_first_boundary(self) -> None:
        ...
    
    async def _read_boundary(self) -> None:
        ...
    
    async def _read_headers(self) -> CIMultiDictProxy[str]:
        ...
    
    async def _maybe_release_last_part(self) -> None:
        """Ensures that the last read body part is read completely."""
        ...
    


_Part = Tuple[Payload, str, str]
class MultipartWriter(Payload):
    """Multipart body writer."""
    def __init__(self, subtype: str = ..., boundary: Optional[str] = ...) -> None:
        ...
    
    def __enter__(self) -> MultipartWriter:
        ...
    
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None:
        ...
    
    def __iter__(self) -> Iterator[_Part]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    _valid_tchar_regex = ...
    _invalid_qdtext_char_regex = ...
    @property
    def _boundary_value(self) -> str:
        """Wrap boundary parameter value in quotes, if necessary.

        Reads self.boundary and returns a unicode sting.
        """
        ...
    
    @property
    def boundary(self) -> str:
        ...
    
    def append(self, obj: Any, headers: Optional[MultiMapping[str]] = ...) -> Payload:
        ...
    
    def append_payload(self, payload: Payload) -> Payload:
        """Adds a new body part to multipart writer."""
        ...
    
    def append_json(self, obj: Any, headers: Optional[MultiMapping[str]] = ...) -> Payload:
        """Helper to append JSON part."""
        ...
    
    def append_form(self, obj: Union[Sequence[Tuple[str, str]], Mapping[str, str]], headers: Optional[MultiMapping[str]] = ...) -> Payload:
        """Helper to append form urlencoded part."""
        ...
    
    @property
    def size(self) -> Optional[int]:
        """Size of the payload."""
        ...
    
    async def write(self, writer: Any, close_boundary: bool = ...) -> None:
        """Write body."""
        ...
    


class MultipartPayloadWriter:
    def __init__(self, writer: Any) -> None:
        ...
    
    def enable_encoding(self, encoding: str) -> None:
        ...
    
    def enable_compression(self, encoding: str = ...) -> None:
        ...
    
    async def write_eof(self) -> None:
        ...
    
    async def write(self, chunk: bytes) -> None:
        ...
    


