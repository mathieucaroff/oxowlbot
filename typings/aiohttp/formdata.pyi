"""
This type stub file was generated by pyright.
"""

from typing import Any, Iterable, Optional
from . import multipart, payload
from .payload import Payload

__all__ = ('FormData', )
class FormData:
    """Helper class for multipart/form-data and
    application/x-www-form-urlencoded body generation."""
    def __init__(self, fields: Iterable[Any] = ..., quote_fields: bool = ..., charset: Optional[str] = ...) -> None:
        ...
    
    @property
    def is_multipart(self) -> bool:
        ...
    
    def add_field(self, name: str, value: Any, *, content_type: Optional[str] = ..., filename: Optional[str] = ..., content_transfer_encoding: Optional[str] = ...) -> None:
        ...
    
    def add_fields(self, *fields: Any) -> None:
        ...
    
    def _gen_form_urlencoded(self) -> payload.BytesPayload:
        ...
    
    def _gen_form_data(self) -> multipart.MultipartWriter:
        """Encode a list of fields using the multipart/form-data MIME format"""
        ...
    
    def __call__(self) -> Payload:
        ...
    


