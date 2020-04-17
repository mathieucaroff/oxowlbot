from typing import NoReturn


def panic(*arg, **kwargs) -> NoReturn:
    raise RuntimeError()
