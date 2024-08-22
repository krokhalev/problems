def lonelyinteger(a):
    data = {}
    for i in a:
        if str(i) in data:
            data[str(i)] = False
        else:
            data[str(i)] = True

    for k, v in data.items():
        if v:
            return int(k)


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))
