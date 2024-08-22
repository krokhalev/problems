def flippingBits(n):
    res2 = []
    res10 = 0
    num = n
    for i in range(32):
        tmp = num % 2
        if tmp == 0:
            res2.insert(0, 1)
        else:
            res2.insert(0, 0)
        num = num // 2

    step = 31
    index = 0
    while True:
        res10 += res2[step] * 2 ** index
        if step == 0:
            break

        step -= 1
        index += 1

    return res10


flippingBits(9)
