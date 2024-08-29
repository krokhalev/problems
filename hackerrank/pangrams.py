def pangrams(s):
    cnt = ord("z") - ord("a")
    sm = 0
    for i in range(cnt + 1):
        sm += i

    res = 0
    data = {}
    for let in s:
        if let == " ":
            continue
        else:
            tmp = ord(let.lower()) - ord("a")
            if str(tmp) in data:
                continue
            data[str(tmp)] = True
            res += tmp

    if res == sm:
        return "pangram"
    return "not pangram"


print(pangrams("We promptly judged antique ivory buckles for the prize"))
