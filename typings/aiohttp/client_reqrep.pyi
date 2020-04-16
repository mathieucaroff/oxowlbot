"""
This type stub file was generated by pyright.
"""

import asyncio
import re
import attr
from types import TracebackType
from typing import Any, Iterable, List, Mapping, Optional, TYPE_CHECKING, Tuple, Type, Union
from multidict import CIMultiDictProxy, MultiDictProxy
from yarl import URL
from . import http
from .abc import AbstractStreamWriter
from .helpers import BaseTimerContext, BasicAuth, HeadersMixin, reify
from .typedefs import JSONDecoder, LooseCookies, LooseHeaders, RawHeaders
from .client import ClientSession
from .connector import Connection
from .tracing import Trace

__all__ = ('ClientRequest', 'ClientResponse', 'RequestInfo', 'Fingerprint')
if TYPE_CHECKING:
    ...
json_re = re.compile(r'^application/(?:[\w.+-]+?\+)?json')
@attr.s(frozen=True, slots=True)
class ContentDisposition:
    type = ...
    parameters = ...
    filename = ...


@attr.s(frozen=True, slots=True)
class RequestInfo:
    url = ...
    method = ...
    headers = ...
    real_url = ...
    @real_url.default
    def real_url_default(self) -> URL:
        ...
    


class Fingerprint:
    HASHFUNC_BY_DIGESTLEN = ...
    def __init__(self, fingerprint: bytes) -> None:
        ...
    
    @property
    def fingerprint(self) -> bytes:
        ...
    
    def check(self, transport: asyncio.Transport) -> None:
        ...
    


if ssl is not None:
    SSL_ALLOWED_TYPES = (ssl.SSLContext, bool, Fingerprint, type(None))
else:
    SSL_ALLOWED_TYPES = type(None)
def _merge_ssl_params(ssl: Union[SSLContext, bool, Fingerprint, None], verify_ssl: Optional[bool], ssl_context: Optional[SSLContext], fingerprint: Optional[bytes]) -> Union[SSLContext, bool, Fingerprint, None]:
    ...

@attr.s(slots=True, frozen=True)
class ConnectionKey:
    host = ...
    port = ...
    is_ssl = ...
    ssl = ...
    proxy = ...
    proxy_auth = ...
    proxy_headers_hash = ...


def _is_expected_content_type(response_content_type: str, expected_content_type: str) -> bool:
    ...

class ClientRequest:
    GET_METHODS = ...
    POST_METHODS = ...
    ALL_METHODS = ...
    DEFAULT_HEADERS = ...
    body = ...
    auth = ...
    response = ...
    _writer = ...
    _continue = ...
    def __init__(self, method: str, url: URL, *, params: Optional[Mapping[str, str]] = ..., headers: Optional[LooseHeaders] = ..., skip_auto_headers: Iterable[str] = ..., data: Any = ..., cookies: Optional[LooseCookies] = ..., auth: Optional[BasicAuth] = ..., version: http.HttpVersion = ..., compress: Optional[str] = ..., chunked: Optional[bool] = ..., expect100: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ..., response_class: Optional[Type[ClientResponse]] = ..., proxy: Optional[URL] = ..., proxy_auth: Optional[BasicAuth] = ..., timer: Optional[BaseTimerContext] = ..., session: Optional[ClientSession] = ..., ssl: Union[SSLContext, bool, Fingerprint, None] = ..., proxy_headers: Optional[LooseHeaders] = ..., traces: Optional[List[Trace]] = ...):
        self.original_url = ...
        self.url = ...
        self.method = ...
        self.chunked = ...
        self.compress = ...
        self.loop = ...
        self.length = ...
        self.response_class = ...
    
    def is_ssl(self) -> bool:
        ...
    
    @property
    def ssl(self) -> Union[SSLContext, None, bool, Fingerprint]:
        ...
    
    @property
    def connection_key(self) -> ConnectionKey:
        ...
    
    @property
    def host(self) -> str:
        ...
    
    @property
    def port(self) -> Optional[int]:
        ...
    
    @property
    def request_info(self) -> RequestInfo:
        ...
    
    def update_host(self, url: URL) -> None:
        """Update destination host, port and connection type (ssl)."""
        ...
    
    def update_version(self, version: Union[http.HttpVersion, str]) -> None:
        """Convert request version to two elements tuple.

        parser HTTP version '1.1' => (1, 1)
        """
        self.version = ...
    
    def update_headers(self, headers: Optional[LooseHeaders]) -> None:
        """Update request headers."""
        self.headers = ...
    
    def update_auto_headers(self, skip_auto_headers: Iterable[str]) -> None:
        self.skip_auto_headers = ...
    
    def update_cookies(self, cookies: Optional[LooseCookies]) -> None:
        """Update request cookies header."""
        ...
    
    def update_content_encoding(self, data: Any) -> None:
        """Set request content encoding."""
        ...
    
    def update_transfer_encoding(self) -> None:
        """Analyze transfer-encoding header."""
        ...
    
    def update_auth(self, auth: Optional[BasicAuth]) -> None:
        """Set basic auth."""
        ...
    
    def update_body_from_data(self, body: Any) -> None:
        self.body = ...
    
    def update_expect_continue(self, expect: bool = ...) -> None:
        ...
    
    def update_proxy(self, proxy: Optional[URL], proxy_auth: Optional[BasicAuth], proxy_headers: Optional[LooseHeaders]) -> None:
        self.proxy = ...
        self.proxy_auth = ...
        self.proxy_headers = ...
    
    def keep_alive(self) -> bool:
        ...
    
    async def write_bytes(self, writer: AbstractStreamWriter, conn: Connection) -> None:
        """Support coroutines that yields bytes objects."""
        ...
    
    async def send(self, conn: Connection) -> ClientResponse:
        self.response = ...
    
    async def close(self) -> None:
        ...
    
    def terminate(self) -> None:
        ...
    
    async def _on_chunk_request_sent(self, chunk: bytes) -> None:
        ...
    


class ClientResponse(HeadersMixin):
    version = ...
    status = ...
    reason = ...
    content = ...
    _headers = ...
    _raw_headers = ...
    _connection = ...
    _source_traceback = ...
    _closed = ...
    _released = ...
    def __init__(self, method: str, url: URL, *, writer: asyncio.Task[None], continue100: Optional[asyncio.Future[bool]], timer: BaseTimerContext, request_info: RequestInfo, traces: List[Trace], loop: asyncio.AbstractEventLoop, session: ClientSession) -> None:
        self.method = ...
        self.cookies = ...
    
    @reify
    def url(self) -> URL:
        ...
    
    @reify
    def url_obj(self) -> URL:
        ...
    
    @reify
    def real_url(self) -> URL:
        ...
    
    @reify
    def host(self) -> str:
        ...
    
    @reify
    def headers(self) -> CIMultiDictProxy[str]:
        ...
    
    @reify
    def raw_headers(self) -> RawHeaders:
        ...
    
    @reify
    def request_info(self) -> RequestInfo:
        ...
    
    @reify
    def content_disposition(self) -> Optional[ContentDisposition]:
        ...
    
    def __del__(self, _warnings: Any = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def connection(self) -> Optional[Connection]:
        ...
    
    @reify
    def history(self) -> Tuple[ClientResponse, ...]:
        """A sequence of of responses, if redirects occurred."""
        ...
    
    @reify
    def links(self) -> MultiDictProxy[MultiDictProxy[Union[str, URL]]]:
        ...
    
    async def start(self, connection: Connection) -> ClientResponse:
        """Start response processing."""
        self.version = ...
        self.status = ...
        self.reason = ...
        self.content = ...
    
    def _response_eof(self) -> None:
        ...
    
    @property
    def closed(self) -> bool:
        ...
    
    def close(self) -> None:
        ...
    
    def release(self) -> Any:
        ...
    
    def raise_for_status(self) -> None:
        ...
    
    def _cleanup_writer(self) -> None:
        ...
    
    def _notify_content(self) -> None:
        ...
    
    async def wait_for_close(self) -> None:
        ...
    
    async def read(self) -> bytes:
        """Read response payload."""
        ...
    
    def get_encoding(self) -> str:
        ...
    
    async def text(self, encoding: Optional[str] = ..., errors: str = ...) -> str:
        """Read response payload and decode."""
        ...
    
    async def json(self, *, encoding: str = ..., loads: JSONDecoder = ..., content_type: Optional[str] = ...) -> Any:
        """Read and decodes JSON response."""
        ...
    
    async def __aenter__(self) -> ClientResponse:
        ...
    
    async def __aexit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None:
        ...
    


