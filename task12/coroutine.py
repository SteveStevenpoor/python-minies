import functools


def coroutine(f):
    @functools.wraps(f)
    def cr(*args, **kwargs):
        gen = f(*args, **kwargs)
        next(gen)
        return gen
    return cr

@coroutine
def storage():
    values = set()
    was_there = False

    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
assert st.send(42) == False
assert st.send(42) == True
assert st.send(21) == False