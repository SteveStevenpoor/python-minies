from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def timed(*args, **kw):
        begin = time()
        result = f(*args, **kw)
        end = time()
        return result, end - begin

    return timed