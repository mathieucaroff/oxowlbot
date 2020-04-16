"""
This type stub file was generated by pyright.
"""

import asyncio
import functools
from types import TracebackType
from typing import Any, Awaitable, Callable, Dict, List, Optional, TYPE_CHECKING, Tuple, Type, Union
from .abc import AbstractResolver
from .client_proto import ResponseHandler
from .client_reqrep import ClientRequest, ConnectionKey, Fingerprint
from .client import ClientTimeout
from .tracing import Trace

__all__ = ('BaseConnector', 'TCPConnector', 'UnixConnector', 'NamedPipeConnector')
if TYPE_CHECKING:
    ...
class _DeprecationWaiter:
    __slots__ = ...
    def __init__(self, awaitable: Awaitable[Any]) -> None:
        ...
    
    def __await__(self) -> Any:
        ...
    
    def __del__(self) -> None:
        ...
    


class Connection:
    _source_traceback = ...
    _transport = ...
    def __init__(self, connector: BaseConnector, key: ConnectionKey, protocol: ResponseHandler, loop: asyncio.AbstractEventLoop) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    def __del__(self, _warnings: Any = ...) -> None:
        ...
    
    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        ...
    
    @property
    def transport(self) -> Optional[asyncio.Transport]:
        ...
    
    @property
    def protocol(self) -> Optional[ResponseHandler]:
        ...
    
    def add_callback(self, callback: Callable[[], None]) -> None:
        ...
    
    def _notify_release(self) -> None:
        ...
    
    def close(self) -> None:
        ...
    
    def release(self) -> None:
        ...
    
    @property
    def closed(self) -> bool:
        ...
    


class _TransportPlaceholder:
    """ placeholder for BaseConnector.connect function """
    def close(self) -> None:
        ...
    


class BaseConnector:
    """Base connector class.

    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    enable_cleanup_closed - Enables clean-up closed ssl transports.
                            Disabled by default.
    loop - Optional event loop.
    """
    _closed = ...
    _source_traceback = ...
    _cleanup_closed_period = ...
    def __init__(self, *, keepalive_timeout: Union[object, None, float] = ..., force_close: bool = ..., limit: int = ..., limit_per_host: int = ..., enable_cleanup_closed: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ...) -> None:
        self.cookies = ...
    
    def __del__(self, _warnings: Any = ...) -> None:
        ...
    
    def __enter__(self) -> BaseConnector:
        ...
    
    def __exit__(self, *exc: Any) -> None:
        ...
    
    async def __aenter__(self) -> BaseConnector:
        ...
    
    async def __aexit__(self, exc_type: Optional[Type[BaseException]] = ..., exc_value: Optional[BaseException] = ..., exc_traceback: Optional[TracebackType] = ...) -> None:
        ...
    
    @property
    def force_close(self) -> bool:
        """Ultimately close connection on releasing if True."""
        ...
    
    @property
    def limit(self) -> int:
        """The total number for simultaneous connections.

        If limit is 0 the connector has no limit.
        The default limit size is 100.
        """
        ...
    
    @property
    def limit_per_host(self) -> int:
        """The limit_per_host for simultaneous connections
        to the same endpoint.

        Endpoints are the same if they are have equal
        (host, port, is_ssl) triple.

        """
        ...
    
    def _cleanup(self) -> None:
        """Cleanup unused transports."""
        ...
    
    def _drop_acquired_per_host(self, key: ConnectionKey, val: ResponseHandler) -> None:
        ...
    
    def _cleanup_closed(self) -> None:
        """Double confirmation for transport close.
        Some broken ssl servers may leave socket open without proper close.
        """
        ...
    
    def close(self) -> Awaitable[None]:
        """Close all opened transports."""
        ...
    
    def _close(self) -> None:
        ...
    
    @property
    def closed(self) -> bool:
        """Is connector closed.

        A readonly property.
        """
        ...
    
    def _available_connections(self, key: ConnectionKey) -> int:
        """
        Return number of available connections taking into account
        the limit, limit_per_host and the connection key.

        If it returns less than 1 means that there is no connections
        availables.
        """
        ...
    
    async def connect(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> Connection:
        """Get from pool or create new connection."""
        ...
    
    def _get(self, key: ConnectionKey) -> Optional[ResponseHandler]:
        ...
    
    def _release_waiter(self) -> None:
        """
        Iterates over all waiters till found one that is not finsihed and
        belongs to a host that has available connections.
        """
        ...
    
    def _release_acquired(self, key: ConnectionKey, proto: ResponseHandler) -> None:
        ...
    
    def _release(self, key: ConnectionKey, protocol: ResponseHandler, *, should_close: bool = ...) -> None:
        ...
    
    async def _create_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> ResponseHandler:
        ...
    


class _DNSCacheTable:
    def __init__(self, ttl: Optional[float] = ...) -> None:
        ...
    
    def __contains__(self, host: object) -> bool:
        ...
    
    def add(self, key: Tuple[str, int], addrs: List[Dict[str, Any]]) -> None:
        ...
    
    def remove(self, key: Tuple[str, int]) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def next_addrs(self, key: Tuple[str, int]) -> List[Dict[str, Any]]:
        ...
    
    def expired(self, key: Tuple[str, int]) -> bool:
        ...
    


class TCPConnector(BaseConnector):
    """TCP connector.

    verify_ssl - Set to True to check ssl certifications.
    fingerprint - Pass the binary sha256
        digest of the expected certificate in DER format to verify
        that the certificate the server presents matches. See also
        https://en.wikipedia.org/wiki/Transport_Layer_Security#Certificate_pinning
    resolver - Enable DNS lookups and use this
        resolver
    use_dns_cache - Use memory cache for DNS lookups.
    ttl_dns_cache - Max seconds having cached a DNS entry, None forever.
    family - socket address family
    local_addr - local tuple of (host, port) to bind socket to

    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    enable_cleanup_closed - Enables clean-up closed ssl transports.
                            Disabled by default.
    loop - Optional event loop.
    """
    def __init__(self, *, verify_ssl: bool = ..., fingerprint: Optional[bytes] = ..., use_dns_cache: bool = ..., ttl_dns_cache: int = ..., family: int = ..., ssl_context: Optional[SSLContext] = ..., ssl: Union[None, bool, Fingerprint, SSLContext] = ..., local_addr: Optional[Tuple[str, int]] = ..., resolver: Optional[AbstractResolver] = ..., keepalive_timeout: Union[None, float, object] = ..., force_close: bool = ..., limit: int = ..., limit_per_host: int = ..., enable_cleanup_closed: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ...):
        ...
    
    def close(self) -> Awaitable[None]:
        """Close all ongoing DNS calls."""
        ...
    
    @property
    def family(self) -> int:
        """Socket family like AF_INET."""
        ...
    
    @property
    def use_dns_cache(self) -> bool:
        """True if local DNS caching is enabled."""
        ...
    
    def clear_dns_cache(self, host: Optional[str] = ..., port: Optional[int] = ...) -> None:
        """Remove specified host/port or clear all dns local cache."""
        ...
    
    async def _resolve_host(self, host: str, port: int, traces: Optional[List[Trace]] = ...) -> List[Dict[str, Any]]:
        ...
    
    async def _create_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> ResponseHandler:
        """Create connection.

        Has same keyword arguments as BaseEventLoop.create_connection.
        """
        ...
    
    @staticmethod
    @functools.lru_cache(None)
    def _make_ssl_context(verified: bool) -> SSLContext:
        ...
    
    def _get_ssl_context(self, req: ClientRequest) -> Optional[SSLContext]:
        """Logic to get the correct SSL context

        0. if req.ssl is false, return None

        1. if ssl_context is specified in req, use it
        2. if _ssl_context is specified in self, use it
        3. otherwise:
            1. if verify_ssl is not specified in req, use self.ssl_context
               (will generate a default context according to self.verify_ssl)
            2. if verify_ssl is True in req, generate a default SSL context
            3. if verify_ssl is False in req, generate a SSL context that
               won't verify
        """
        ...
    
    def _get_fingerprint(self, req: ClientRequest) -> Optional[Fingerprint]:
        ...
    
    async def _wrap_create_connection(self, *args: Any, req: ClientRequest, timeout: ClientTimeout, client_error: Type[Exception] = ..., **kwargs: Any) -> Tuple[asyncio.Transport, ResponseHandler]:
        ...
    
    async def _create_direct_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout, *, client_error: Type[Exception] = ...) -> Tuple[asyncio.Transport, ResponseHandler]:
        ...
    
    async def _create_proxy_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> Tuple[asyncio.Transport, ResponseHandler]:
        ...
    


class UnixConnector(BaseConnector):
    """Unix socket connector.

    path - Unix socket path.
    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    loop - Optional event loop.
    """
    def __init__(self, path: str, force_close: bool = ..., keepalive_timeout: Union[object, float, None] = ..., limit: int = ..., limit_per_host: int = ..., loop: Optional[asyncio.AbstractEventLoop] = ...) -> None:
        ...
    
    @property
    def path(self) -> str:
        """Path to unix socket."""
        ...
    
    async def _create_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> ResponseHandler:
        ...
    


class NamedPipeConnector(BaseConnector):
    """Named pipe connector.

    Only supported by the proactor event loop.
    See also: https://docs.python.org/3.7/library/asyncio-eventloop.html

    path - Windows named pipe path.
    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    loop - Optional event loop.
    """
    def __init__(self, path: str, force_close: bool = ..., keepalive_timeout: Union[object, float, None] = ..., limit: int = ..., limit_per_host: int = ..., loop: Optional[asyncio.AbstractEventLoop] = ...) -> None:
        ...
    
    @property
    def path(self) -> str:
        """Path to the named pipe."""
        ...
    
    async def _create_connection(self, req: ClientRequest, traces: List[Trace], timeout: ClientTimeout) -> ResponseHandler:
        ...
    


