import functools


def deprecated(f = None, *, since = '', will_be_removed = ''):
    if f is None:
        return functools.partial(deprecated, since = since, will_be_removed = will_be_removed)

    since = f' since version {since}' if since else ''
    will_be_removed = f'version {will_be_removed}' if will_be_removed else 'future versions'

    @functools.wraps(f)
    def inner(*args, **kwargs):
        warning = f'Warning: function {f.__name__} is deprecated{since}. '
        warning += f'It will be removed in {will_be_removed}.'
        print(warning)

        res = f(*args, **kwargs)
        return res

    return inner

@deprecated(since='4.2.0', will_be_removed='5.0.1')
def foo():
    print('Hello from foo')

@deprecated(since='4.2.0')
def bar():
    print('Hello from bar')

@deprecated(will_be_removed='5.0.1')
def baz():
    print('Hello from baz')

@deprecated
def aboba():
    print('Hello from aboba')

foo()
bar()
baz()
aboba()
