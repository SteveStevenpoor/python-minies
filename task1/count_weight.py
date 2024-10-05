#This function counts weight of an integer
def count_weight(x: int) -> int:
    count = 0
    cmpr = 0
    if x < 0:
        cmpr = 1
        count += 1

    while abs(x) > cmpr:
        if x & 1:
            count += 1
        x = x >> 1

    return count

