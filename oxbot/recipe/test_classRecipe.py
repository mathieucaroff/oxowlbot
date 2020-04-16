import pytest
from .classRecipe import ClassRecipe


should_accept = """
Who is a kirin?
Who is an alicorn?
Who is dragon?
""".strip().split(
    "\n"
)

should_reject = """
Who?
Who are they?
Who is Apple Bloom?
""".strip().split(
    "\n"
)


@pytest.mark.parametrize(
    "input,expected",
    [*zip(should_accept, [True] * 99), *zip(should_reject, [False] * 99),],
)
def test_match(input: str, expected: bool):
    assert ClassRecipe().match(input) == expected
