# This function return matrix from string format 'a00 a01 | a10 a11'
def stomat(s: str) -> list:
    res_mat = []
    str_list = s.split()

    row = []
    for c in str_list:
        if c == '|':
            res_mat.append(row)
            row = []
        else:
            row.append(float(c))
    res_mat.append(row)

    return res_mat
