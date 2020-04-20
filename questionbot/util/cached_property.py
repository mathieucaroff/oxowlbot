from functools import wraps
from typing import Callable, TypeVar, cast


R = TypeVar('R')
S = TypeVar('S')


def cached_property(f: Callable[[S], R]):
    """a @property decorator which caches results"""

    @wraps(f)
    def get(self: S) -> R:
        try:
            return self._property_cache[f]
        except AttributeError:
            self._property_cache = {}
            x = self._property_cache[f] = f(self)
            return x
        except KeyError:
            x = self._property_cache[f] = f(self)
            return x

    return cast(R, property(cast(Callable[[S], R], get)))
