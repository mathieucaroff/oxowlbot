"""
This type stub file was generated by pyright.
"""

from typing import Awaitable, Callable, TYPE_CHECKING, Tuple, Type, TypeVar
from .web_exceptions import _HTTPMove
from .web_request import Request
from .web_response import StreamResponse
from .web_app import Application

__all__ = ('middleware', 'normalize_path_middleware')
if TYPE_CHECKING:
    ...
_Func = TypeVar('_Func')
async def _check_request_resolves(request: Request, path: str) -> Tuple[bool, Request]:
    ...

def middleware(f: _Func) -> _Func:
    ...

_Handler = Callable[[Request], Awaitable[StreamResponse]]
_Middleware = Callable[[Request, _Handler], Awaitable[StreamResponse]]
def normalize_path_middleware(*, append_slash: bool = ..., remove_slash: bool = ..., merge_slashes: bool = ..., redirect_class: Type[_HTTPMove] = ...) -> _Middleware:
    """
    Middleware factory which produces a middleware that normalizes
    the path of a request. By normalizing it means:

        - Add or remove a trailing slash to the path.
        - Double slashes are replaced by one.

    The middleware returns as soon as it finds a path that resolves
    correctly. The order if both merge and append/remove are enabled is
        1) merge slashes
        2) append/remove slash
        3) both merge slashes and append/remove slash.
    If the path resolves with at least one of those conditions, it will
    redirect to the new path.

    Only one of `append_slash` and `remove_slash` can be enabled. If both
    are `True` the factory will raise an assertion error

    If `append_slash` is `True` the middleware will append a slash when
    needed. If a resource is defined with trailing slash and the request
    comes without it, it will append it automatically.

    If `remove_slash` is `True`, `append_slash` must be `False`. When enabled
    the middleware will remove trailing slashes and redirect if the resource
    is defined

    If merge_slashes is True, merge multiple consecutive slashes in the
    path into one.
    """
    ...

def _fix_request_current_app(app: Application) -> _Middleware:
    ...

