from oxbot.oxbot import Oxbot
import trio  # type: ignore


async def test_do_not_raise():
    try:
        await Oxbot().process("Hello!")
    except Exception:
        import sys, traceback

        traceback.print_exc(file=sys.stderr)
        raise
    return
