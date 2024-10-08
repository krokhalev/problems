def twoArrays(k, a, b):

    a.sort(reverse=True)

    b.sort()

    for i in range(len(a)):
        if (a[i] + b[i] < k):
            return "NO"

    return "YES"


def result(index, stng):
    answers = ["NO", "YES", "NO", "NO", "YES", "NO", "NO", "YES", "NO", "YES", "YES", "NO"]
    if stng == answers[index]:
        print(stng)
    else:
        print(f"'{stng}' IS WRONG RESULT, CORRECT IS '{answers[index]}'")


result(0, twoArrays(91, [18, 73, 55, 59, 37, 13, 1, 33], [81, 11, 77, 49, 65, 26, 29, 49, ]))
result(1, twoArrays(94, [84, 2, 50, 51, 19, 58, 12, 90, 81, 68, 54, 73, 81, 31, 79, 85, 39, 2],
                    [53, 102, 40, 17, 33, 92, 18, 79, 66, 23, 84, 25, 38, 43, 27, 55, 8, 19]))
result(2, twoArrays(88, [66, 66, 32, 75, 77, 34, 23, 35], [61, 17, 52, 20, 48, 11, 50, 5]))
result(3, twoArrays(45, [11, 16, 43, 5, 25, 22, 19, 32, 10, 26, 2, 42, 16, 1],
                    [33, 1, 1, 20, 26, 7, 17, 39, 23, 34, 10, 11, 38, 20]))
result(4, twoArrays(59, [15, 16, 44, 58, 5, 10, 16, 9, 4, 20, 24], [37, 45, 41, 46, 8, 23, 59, 57, 51, 44, 59]))
result(5, twoArrays(32, [28, 14, 24, 25, 2, 20, 1, 26], [4, 3, 1, 11, 25, 22, 2, 4]))
result(6, twoArrays(57, [1, 7, 42, 26, 45, 14], [37, 49, 42, 26, 4, 11]))
result(7, twoArrays(88, [25, 60, 49, 4], [65, 46, 85, 34]))
result(8,
       twoArrays(9, [2, 1, 1, 4, 1, 7, 3, 4, 3, 7, 3, 1, 3, 5, 6, 7], [1, 1, 1, 1, 4, 1, 2, 1, 7, 1, 1, 1, 1, 1, 1, 2]))
result(9, twoArrays(70, [40], [38]))
