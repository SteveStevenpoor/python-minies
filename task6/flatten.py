
def flatten(l: list, depth = None) -> list:
    """This function makes a list flat."""
    res = list()

    def rec_traverse(el, depth):
        if isinstance(el, list) and (depth is None or depth >= 0):
            for x in el:
                rec_traverse(x, depth if depth is None else depth - 1)
        else:
            res.append(el)

    rec_traverse(l, depth)
    return res
