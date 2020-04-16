"""
This type stub file was generated by pyright.
"""

import abc
import re
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Awaitable, Callable, Container, Dict, Generator, Iterable, Iterator, List, Mapping, Optional, Set, Sized, TYPE_CHECKING, Tuple, Type, Union
from yarl import URL
from .abc import AbstractMatchInfo, AbstractRouter, AbstractView
from .typedefs import PathLike
from .web_exceptions import HTTPException
from .web_request import Request
from .web_response import StreamResponse
from .web_routedef import AbstractRouteDef
from .web_app import Application

__all__ = ('UrlDispatcher', 'UrlMappingMatchInfo', 'AbstractResource', 'Resource', 'PlainResource', 'DynamicResource', 'AbstractRoute', 'ResourceRoute', 'StaticResource', 'View')
if TYPE_CHECKING:
    BaseDict = Dict[str, str]
else:
    ...
HTTP_METHOD_RE = re.compile(r"^[0-9A-Za-z!#\$%&'\*\+\-\.\^_`\|~]+$")
ROUTE_RE = re.compile(r'(\{[_a-zA-Z][^{}]*(?:\{[^{}]*\}[^{}]*)*\})')
PATH_SEP = re.escape('/')
_WebHandler = Callable[[Request], Awaitable[StreamResponse]]
_ExpectHandler = Callable[[Request], Awaitable[None]]
_Resolve = Tuple[Optional[AbstractMatchInfo], Set[str]]
class AbstractResource(Sized, Iterable['AbstractRoute']):
    def __init__(self, *, name: Optional[str] = ...) -> None:
        ...
    
    @property
    def name(self) -> Optional[str]:
        ...
    
    @property
    @abc.abstractmethod
    def canonical(self) -> str:
        """Exposes the resource's canonical path.

        For example '/foo/bar/{name}'

        """
        ...
    
    @abc.abstractmethod
    def url_for(self, **kwargs: str) -> URL:
        """Construct url for resource with additional params."""
        ...
    
    @abc.abstractmethod
    async def resolve(self, request: Request) -> _Resolve:
        """Resolve resource

        Return (UrlMappingMatchInfo, allowed_methods) pair."""
        ...
    
    @abc.abstractmethod
    def add_prefix(self, prefix: str) -> None:
        """Add a prefix to processed URLs.

        Required for subapplications support.

        """
        ...
    
    @abc.abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Return a dict with additional info useful for introspection"""
        ...
    
    def freeze(self) -> None:
        ...
    
    @abc.abstractmethod
    def raw_match(self, path: str) -> bool:
        """Perform a raw match against path"""
        ...
    


class AbstractRoute(abc.ABC):
    def __init__(self, method: str, handler: Union[_WebHandler, Type[AbstractView]], *, expect_handler: _ExpectHandler = ..., resource: AbstractResource = ...) -> None:
        ...
    
    @property
    def method(self) -> str:
        ...
    
    @property
    def handler(self) -> _WebHandler:
        ...
    
    @property
    @abc.abstractmethod
    def name(self) -> Optional[str]:
        """Optional route's name, always equals to resource's name."""
        ...
    
    @property
    def resource(self) -> Optional[AbstractResource]:
        ...
    
    @abc.abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Return a dict with additional info useful for introspection"""
        ...
    
    @abc.abstractmethod
    def url_for(self, *args: str, **kwargs: str) -> URL:
        """Construct url for route with additional params."""
        ...
    
    async def handle_expect_header(self, request: Request) -> None:
        ...
    


class UrlMappingMatchInfo(BaseDict, AbstractMatchInfo):
    def __init__(self, match_dict: Dict[str, str], route: AbstractRoute):
        ...
    
    @property
    def handler(self) -> _WebHandler:
        ...
    
    @property
    def route(self) -> AbstractRoute:
        ...
    
    @property
    def expect_handler(self) -> _ExpectHandler:
        ...
    
    @property
    def http_exception(self) -> Optional[HTTPException]:
        ...
    
    def get_info(self) -> Dict[str, str]:
        ...
    
    @property
    def apps(self) -> Tuple[Application, ...]:
        ...
    
    def add_app(self, app: Application) -> None:
        ...
    
    @property
    def current_app(self) -> Application:
        ...
    
    @contextmanager
    def set_current_app(self, app: Application) -> Generator[None, None, None]:
        ...
    
    def freeze(self) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    


class MatchInfoError(UrlMappingMatchInfo):
    def __init__(self, http_exception: HTTPException) -> None:
        ...
    
    @property
    def http_exception(self) -> HTTPException:
        ...
    
    def __repr__(self) -> str:
        ...
    


async def _default_expect_handler(request: Request) -> None:
    """Default handler for Expect header.

    Just send "100 Continue" to client.
    raise HTTPExpectationFailed if value of header is not "100-continue"
    """
    ...

class Resource(AbstractResource):
    def __init__(self, *, name: Optional[str] = ...) -> None:
        ...
    
    def add_route(self, method: str, handler: Union[Type[AbstractView], _WebHandler], *, expect_handler: Optional[_ExpectHandler] = ...) -> ResourceRoute:
        ...
    
    def register_route(self, route: ResourceRoute) -> None:
        ...
    
    async def resolve(self, request: Request) -> _Resolve:
        ...
    
    @abc.abstractmethod
    def _match(self, path: str) -> Optional[Dict[str, str]]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[AbstractRoute]:
        ...
    


class PlainResource(Resource):
    def __init__(self, path: str, *, name: Optional[str] = ...) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def freeze(self) -> None:
        ...
    
    def add_prefix(self, prefix: str) -> None:
        ...
    
    def _match(self, path: str) -> Optional[Dict[str, str]]:
        ...
    
    def raw_match(self, path: str) -> bool:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    def url_for(self) -> URL:
        ...
    
    def __repr__(self) -> str:
        ...
    


class DynamicResource(Resource):
    DYN = ...
    DYN_WITH_RE = ...
    GOOD = ...
    def __init__(self, path: str, *, name: Optional[str] = ...) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def add_prefix(self, prefix: str) -> None:
        ...
    
    def _match(self, path: str) -> Optional[Dict[str, str]]:
        ...
    
    def raw_match(self, path: str) -> bool:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    def url_for(self, **parts: str) -> URL:
        ...
    
    def __repr__(self) -> str:
        ...
    


class PrefixResource(AbstractResource):
    def __init__(self, prefix: str, *, name: Optional[str] = ...) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def add_prefix(self, prefix: str) -> None:
        ...
    
    def raw_match(self, prefix: str) -> bool:
        ...
    


class StaticResource(PrefixResource):
    VERSION_KEY = ...
    def __init__(self, prefix: str, directory: PathLike, *, name: Optional[str] = ..., expect_handler: Optional[_ExpectHandler] = ..., chunk_size: int = ..., show_index: bool = ..., follow_symlinks: bool = ..., append_version: bool = ...) -> None:
        ...
    
    def url_for(self, *, filename: Union[str, Path], append_version: Optional[bool] = ...) -> URL:
        ...
    
    @staticmethod
    def _get_file_hash(byte_array: bytes) -> str:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    def set_options_route(self, handler: _WebHandler) -> None:
        ...
    
    async def resolve(self, request: Request) -> _Resolve:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[AbstractRoute]:
        ...
    
    async def _handle(self, request: Request) -> StreamResponse:
        ...
    
    def _directory_as_html(self, filepath: Path) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    


class PrefixedSubAppResource(PrefixResource):
    def __init__(self, prefix: str, app: Application) -> None:
        ...
    
    def add_prefix(self, prefix: str) -> None:
        ...
    
    def url_for(self, *args: str, **kwargs: str) -> URL:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    async def resolve(self, request: Request) -> _Resolve:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[AbstractRoute]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class AbstractRuleMatching(abc.ABC):
    @abc.abstractmethod
    async def match(self, request: Request) -> bool:
        """Return bool if the request satisfies the criteria"""
        ...
    
    @abc.abstractmethod
    def get_info(self) -> Dict[str, Any]:
        """Return a dict with additional info useful for introspection"""
        ...
    
    @property
    @abc.abstractmethod
    def canonical(self) -> str:
        """Return a str"""
        ...
    


class Domain(AbstractRuleMatching):
    re_part = ...
    def __init__(self, domain: str) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def validation(self, domain: str) -> str:
        ...
    
    async def match(self, request: Request) -> bool:
        ...
    
    def match_domain(self, host: str) -> bool:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    


class MaskDomain(Domain):
    re_part = ...
    def __init__(self, domain: str) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def match_domain(self, host: str) -> bool:
        ...
    


class MatchedSubAppResource(PrefixedSubAppResource):
    def __init__(self, rule: AbstractRuleMatching, app: Application) -> None:
        ...
    
    @property
    def canonical(self) -> str:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    async def resolve(self, request: Request) -> _Resolve:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ResourceRoute(AbstractRoute):
    """A route with resource"""
    def __init__(self, method: str, handler: Union[_WebHandler, Type[AbstractView]], resource: AbstractResource, *, expect_handler: Optional[_ExpectHandler] = ...) -> None:
        ...
    
    def __repr__(self) -> str:
        ...
    
    @property
    def name(self) -> Optional[str]:
        ...
    
    def url_for(self, *args: str, **kwargs: str) -> URL:
        """Construct url for route with additional params."""
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    


class SystemRoute(AbstractRoute):
    def __init__(self, http_exception: HTTPException) -> None:
        ...
    
    def url_for(self, *args: str, **kwargs: str) -> URL:
        ...
    
    @property
    def name(self) -> Optional[str]:
        ...
    
    def get_info(self) -> Dict[str, Any]:
        ...
    
    async def _handle(self, request: Request) -> StreamResponse:
        ...
    
    @property
    def status(self) -> int:
        ...
    
    @property
    def reason(self) -> str:
        ...
    
    def __repr__(self) -> str:
        ...
    


class View(AbstractView):
    async def _iter(self) -> StreamResponse:
        ...
    
    def __await__(self) -> Generator[Any, None, StreamResponse]:
        ...
    
    def _raise_allowed_methods(self) -> None:
        ...
    


class ResourcesView(Sized, Iterable[AbstractResource], Container[AbstractResource]):
    def __init__(self, resources: List[AbstractResource]) -> None:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[AbstractResource]:
        ...
    
    def __contains__(self, resource: object) -> bool:
        ...
    


class RoutesView(Sized, Iterable[AbstractRoute], Container[AbstractRoute]):
    def __init__(self, resources: List[AbstractResource]):
        ...
    
    def __len__(self) -> int:
        ...
    
    def __iter__(self) -> Iterator[AbstractRoute]:
        ...
    
    def __contains__(self, route: object) -> bool:
        ...
    


class UrlDispatcher(AbstractRouter, Mapping[str, AbstractResource]):
    NAME_SPLIT_RE = ...
    def __init__(self) -> None:
        ...
    
    async def resolve(self, request: Request) -> AbstractMatchInfo:
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __contains__(self, resource: object) -> bool:
        ...
    
    def __getitem__(self, name: str) -> AbstractResource:
        ...
    
    def resources(self) -> ResourcesView:
        ...
    
    def routes(self) -> RoutesView:
        ...
    
    def named_resources(self) -> Mapping[str, AbstractResource]:
        ...
    
    def register_resource(self, resource: AbstractResource) -> None:
        ...
    
    def add_resource(self, path: str, *, name: Optional[str] = ...) -> Resource:
        ...
    
    def add_route(self, method: str, path: str, handler: Union[_WebHandler, Type[AbstractView]], *, name: Optional[str] = ..., expect_handler: Optional[_ExpectHandler] = ...) -> AbstractRoute:
        ...
    
    def add_static(self, prefix: str, path: PathLike, *, name: Optional[str] = ..., expect_handler: Optional[_ExpectHandler] = ..., chunk_size: int = ..., show_index: bool = ..., follow_symlinks: bool = ..., append_version: bool = ...) -> AbstractResource:
        """Add static files view.

        prefix - url prefix
        path - folder with files

        """
        ...
    
    def add_head(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method HEAD
        """
        ...
    
    def add_options(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method OPTIONS
        """
        ...
    
    def add_get(self, path: str, handler: _WebHandler, *, name: Optional[str] = ..., allow_head: bool = ..., **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method GET, if allow_head is true another
        route is added allowing head requests to the same endpoint
        """
        ...
    
    def add_post(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method POST
        """
        ...
    
    def add_put(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method PUT
        """
        ...
    
    def add_patch(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method PATCH
        """
        ...
    
    def add_delete(self, path: str, handler: _WebHandler, **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with method DELETE
        """
        ...
    
    def add_view(self, path: str, handler: Type[AbstractView], **kwargs: Any) -> AbstractRoute:
        """
        Shortcut for add_route with ANY methods for a class-based view
        """
        ...
    
    def freeze(self) -> None:
        ...
    
    def add_routes(self, routes: Iterable[AbstractRouteDef]) -> None:
        """Append routes to route table.

        Parameter should be a sequence of RouteDef objects.
        """
        ...
    


