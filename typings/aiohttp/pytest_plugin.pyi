"""
This type stub file was generated by pyright.
"""

import contextlib
import pytest

def pytest_addoption(parser):
    ...

def pytest_fixture_setup(fixturedef):
    """
    Allow fixtures to be coroutines. Run coroutine fixtures in an event loop.
    """
    ...

@pytest.fixture
def fast(request):
    """--fast config option"""
    ...

@pytest.fixture
def loop_debug(request):
    """--enable-loop-debug config option"""
    ...

@contextlib.contextmanager
def _runtime_warning_context():
    """
    Context manager which checks for RuntimeWarnings, specifically to
    avoid "coroutine 'X' was never awaited" warnings being missed.

    If RuntimeWarnings occur in the context a RuntimeError is raised.
    """
    ...

@contextlib.contextmanager
def _passthrough_loop_context(loop, fast: bool = ...):
    """
    setups and tears down a loop unless one is passed in via the loop
    argument when it's passed straight through.
    """
    ...

def pytest_pycollect_makeitem(collector, name, obj):
    """
    Fix pytest collecting for coroutines.
    """
    ...

def pytest_pyfunc_call(pyfuncitem):
    """
    Run coroutines in an event loop instead of a normal function call.
    """
    ...

def pytest_generate_tests(metafunc):
    ...

@pytest.fixture
def loop(loop_factory, fast, loop_debug):
    """Return an instance of the event loop."""
    ...

@pytest.fixture
def proactor_loop():
    ...

@pytest.fixture
def unused_port(aiohttp_unused_port):
    ...

@pytest.fixture
def aiohttp_unused_port():
    """Return a port that is unused on the current host."""
    ...

@pytest.fixture
def aiohttp_server(loop):
    """Factory to create a TestServer instance, given an app.

    aiohttp_server(app, **kwargs)
    """
    ...

@pytest.fixture
def test_server(aiohttp_server):
    ...

@pytest.fixture
def aiohttp_raw_server(loop):
    """Factory to create a RawTestServer instance, given a web handler.

    aiohttp_raw_server(handler, **kwargs)
    """
    ...

@pytest.fixture
def raw_test_server(aiohttp_raw_server):
    ...

@pytest.fixture
def aiohttp_client(loop):
    """Factory to create a TestClient instance.

    aiohttp_client(app, **kwargs)
    aiohttp_client(server, **kwargs)
    aiohttp_client(raw_server, **kwargs)
    """
    ...

@pytest.fixture
def test_client(aiohttp_client):
    ...

