import functools
import logging

logging.basicConfig(level=logging.DEBUG)


class log(object):
    def __init__(self, name=""):
        loggerName = '@log'
        if name:
            loggerName = f"{loggerName} {name}"
        self.logger = logging.getLogger(loggerName)

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            try:
                self.logger.debug("/\\ {0} - {1} - {2}".format(fn.__name__, args, kwargs))
                result = fn(*args, **kwargs)
                self.logger.debug(f"\\/ {result}")
                return result
            except Exception as ex:
                self.logger.debug("Exception {0}".format(ex))
                raise ex
            return result
        return decorated
