def plusMinus(arr):
    len_arr = len(arr)
    data = {
        "pos": 0,
        "neg": 0,
        "zero": 0
    }

    for i in arr:
        if i == 0:
            data["zero"] += 1
        if i > 0:
            data["pos"] += 1
        if i < 0:
            data["neg"] += 1

    for k, v in data.items():
        print(round(v / len_arr, 6))


plusMinus([1, 1, 0, -1, -1])
