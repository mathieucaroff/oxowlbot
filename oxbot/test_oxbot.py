from oxbot.oxbot import Oxbot

import pytest
import trio


async def test_do_not_raise():
    try:
        await Oxbot().process("Hello!")
    except Exception:
        import sys, traceback

        traceback.print_exc(file=sys.stderr)
        raise
    return


async def test_info_length():
    result = await Oxbot().process("Hello there!")
    assert len(result.info.split("\n")) == 3


@pytest.mark.skip()
async def test_stanza_serialize():
    import stanza

    nlp = stanza.Pipeline("en")
    result = nlp("Hello there!")
    json_result = str(result)
