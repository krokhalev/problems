def matchingStrings(strings, queries):
    res = [0] * len(queries)
    for i in range(len(queries)):
        for s in strings:
            if queries[i] == s:
                res[i] += 1
    return res


s = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
q = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]
matchingStrings(s, q)
