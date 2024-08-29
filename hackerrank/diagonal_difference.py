def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    len_mtx = len(arr)
    len_row = len(arr[0])
    itr = 0

    for i in range(len_mtx):
        d1 += arr[i][itr]
        d2 += arr[i][len_row - 1 - itr]
        itr += 1

    res = d1 - d2
    if res < 0:
        return res * -1

    return res


print(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))
