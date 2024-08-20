def reverse(arr):
    for i in range(len(arr)):
        left = arr[i]
        right = arr[len(arr)-1-i]
        arr[i] = right
        arr[len(arr)-1-i] = left
        if i >= len(arr)-1-i:
            return arr


print(reverse([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
