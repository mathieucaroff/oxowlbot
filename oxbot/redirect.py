import sys
from contextlib import contextmanager
import io
from typing import Any, cast


@contextmanager
def redirect(stdName: str, handle: io.IOBase = None):
    if handle is None:
        handle = cast(Any, io.StringIO())
    handle_backup = getattr(sys, stdName)
    try:
        setattr(sys, stdName, handle)
        yield handle
    finally:
        setattr(sys, stdName, handle_backup)


def redirect_stdin(handle: io.IOBase = None):
    return redirect("stdin", handle)


def redirect_stdout(handle: io.IOBase = None):
    return redirect("stdout", handle)


def redirect_stderr(handle: io.IOBase = None):
    return redirect("stderr", handle)


@contextmanager
def redirect_all(handle: io.IOBase = None):
    if handle is None:
        handle = cast(Any, io.StringIO())
    with redirect("stdin", handle):
        with redirect("stdout", handle):
            with redirect("stderr", handle):
                yield handle
