import pytest

from .classRecipe import ClassRecipe
from ..parsing import ParseSuccess_word_list, Parser
from ..stanzaProvider import createStanzaWebPipeline
from typing import Any, Awaitable, cast


parser = Parser(createStanzaWebPipeline())


async def normalSentence(sentence: str) -> Awaitable[str]:
    parse_result = await parser.parse(sentence)

    assert isinstance(parse_result, ParseSuccess_word_list)

    return cast(Any, parse_result).normalSentence


should_accept = """
Who is a kirin?
Who is a kirin
Who is kirin
Who are kirin
Who are a kirin
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
async def test_match(input: Awaitable[str], expected: bool):
    assert ClassRecipe().match(await normalSentence(input)) == expected
