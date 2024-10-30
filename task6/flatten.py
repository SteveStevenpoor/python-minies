
def flatten(l: list, depth = None) -> list:
    """This function makes a list flat."""
    res = list()

    def rec_traverse(el, depth):
        if isinstance(el, list):
            if depth is None:
                for x in el:
                    rec_traverse(x, depth)
            elif depth >= 0:
                for x in el:
                    rec_traverse(x, depth - 1)
            else:
                res.append(el)
        else:
            res.append(el)

    rec_traverse(l, depth)
    return res
