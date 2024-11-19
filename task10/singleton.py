import functools


def singleton(cls):
    orig_new = cls.__new__
    single_obj = None

    @functools.wraps(orig_new)
    def singleton_new(cls, *args, **kwargs):
        nonlocal single_obj
        if single_obj is None:
            single_obj = orig_new(cls)
        return single_obj

    cls.__new__ = singleton_new

    return cls

@singleton
class TestClass:
    def __init__(self, name: str):
        self.name = name


t1 = TestClass('aboba')
t2 = TestClass('not aboba')
t3 = TestClass('even not not aboba')
assert (id(t1) == id(t2))
assert (id(t1) == id(t3))
assert (id(t2) == id(t3))
