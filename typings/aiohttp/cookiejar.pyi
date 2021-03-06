"""
This type stub file was generated by pyright.
"""

import asyncio
import datetime
from http.cookies import BaseCookie, Morsel
from typing import Iterator, Optional, Union
from yarl import URL
from .abc import AbstractCookieJar
from .typedefs import LooseCookies, PathLike

__all__ = ('CookieJar', 'DummyCookieJar')
CookieItem = Union[str, 'Morsel[str]']
class CookieJar(AbstractCookieJar):
    """Implements cookie storage adhering to RFC 6265."""
    DATE_TOKENS_RE = ...
    DATE_HMS_TIME_RE = ...
    DATE_DAY_OF_MONTH_RE = ...
    DATE_MONTH_RE = ...
    DATE_YEAR_RE = ...
    MAX_TIME = ...
    def __init__(self, *, unsafe: bool = ..., loop: Optional[asyncio.AbstractEventLoop] = ...) -> None:
        ...
    
    def save(self, file_path: PathLike) -> None:
        ...
    
    def load(self, file_path: PathLike) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def __iter__(self) -> Iterator[Morsel[str]]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def _do_expiration(self) -> None:
        ...
    
    def _expire_cookie(self, when: datetime.datetime, domain: str, name: str) -> None:
        ...
    
    def update_cookies(self, cookies: LooseCookies, response_url: URL = ...) -> None:
        """Update cookies."""
        ...
    
    def filter_cookies(self, request_url: URL = ...) -> BaseCookie[str]:
        """Returns this jar's cookies filtered by their attributes."""
        ...
    
    @staticmethod
    def _is_domain_match(domain: str, hostname: str) -> bool:
        """Implements domain matching adhering to RFC 6265."""
        ...
    
    @staticmethod
    def _is_path_match(req_path: str, cookie_path: str) -> bool:
        """Implements path matching adhering to RFC 6265."""
        ...
    
    @classmethod
    def _parse_date(cls, date_str: str) -> Optional[datetime.datetime]:
        """Implements date string parsing adhering to RFC 6265."""
        ...
    


class DummyCookieJar(AbstractCookieJar):
    """Implements a dummy cookie storage.

    It can be used with the ClientSession when no cookie processing is needed.

    """
    def __init__(self, *, loop: Optional[asyncio.AbstractEventLoop] = ...) -> None:
        ...
    
    def __iter__(self) -> Iterator[Morsel[str]]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def clear(self) -> None:
        ...
    
    def update_cookies(self, cookies: LooseCookies, response_url: URL = ...) -> None:
        ...
    
    def filter_cookies(self, request_url: URL) -> BaseCookie[str]:
        ...
    


