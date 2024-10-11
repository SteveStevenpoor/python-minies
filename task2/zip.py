# This function creates mapped list of 2 lists

def my_zip(l1: list, l2: list) -> list:
    return [(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]