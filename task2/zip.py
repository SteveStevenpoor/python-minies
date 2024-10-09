# This function creates mapped list of 2 lists

def my_zip(l1: list, l2: list) -> list:
    result = []
    n = len(l1) if len(l1) < len(l2) else len(l2)

    for i in range(n):
        result.append((l1[i], l2[i]))

    return result
