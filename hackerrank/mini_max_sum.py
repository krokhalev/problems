def miniMaxSum(arr):
    max_sum = 0
    min_sum = 0

    for i in range(len(arr)):
        res = sum(arr[:i] + arr[i + 1:])
        if i == 0:
            min_sum = res
        if res > max_sum:
            max_sum = res
        if res < min_sum:
            min_sum = res

    print(min_sum, max_sum)


miniMaxSum([1, 3, 5, 7, 9])
