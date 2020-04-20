from typing import Any, List, Tuple, TypeVar, cast


T = TypeVar('T')

def tuple2(li: List[List[T]]) -> List[Tuple[T, T]]:
    return cast(Any, li)