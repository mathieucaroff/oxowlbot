"""
This type stub file was generated by pyright.
"""

class FileProxyMixin:
    @property
    def closed(self) -> bool:
        ...
    
    def readable(self) -> bool:
        ...
    
    def writable(self) -> bool:
        ...
    
    def seekable(self) -> bool:
        ...
    
    def __iter__(self):
        ...
    


