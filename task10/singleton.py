import functools


def singleton(cls):
    orig_new = cls.__new__
    orig_init = cls.__init__

    initialized = False
    single_obj = None

    @functools.wraps(orig_new)
    def singleton_new(cls, *args, **kwargs):
        nonlocal single_obj
        if single_obj is None:
            single_obj = orig_new(cls)
        return single_obj

    @functools.wraps(orig_new)
    def singleton_init(cls, *args, **kwargs):
        nonlocal single_obj
        nonlocal initialized
        if not initialized:
            orig_init(single_obj, *args, **kwargs)
            initialized = True

    cls.__new__ = singleton_new
    cls.__init__ = singleton_init

    return cls


@singleton
class TestClass:
    def __init__(self, name: str):
        self.name = name
        print(name)


t1 = TestClass('aboba')
t2 = TestClass('not aboba')
t3 = TestClass('even not not aboba')
assert (id(t1) == id(t2))
assert (id(t1) == id(t3))
assert (id(t2) == id(t3))
assert (t1.name == t2.name)
assert (t1.name == t3.name)
assert (t3.name == t2.name)
