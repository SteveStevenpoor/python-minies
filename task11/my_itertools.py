def cycle(iterable):
    while True:
        yield from iterable


def chain(*iterables):
    for iterable in iterables:
        yield from iterable
