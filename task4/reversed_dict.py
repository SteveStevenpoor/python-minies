# This function reverse key, value pairs in python dictionary
def give_reversed_dict(orig_dict: dict) -> dict:
    rev_dict = {}
    for key, value in orig_dict.items():
        if rev_dict.get(value):
            if isinstance(rev_dict[value], tuple):
                rev_dict[value] += (key,)
            else:
                rev_dict[value] = (rev_dict[value], key)
        else:
            rev_dict[value] = key

    return rev_dict
