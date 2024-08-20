def sravnenie(str1, str2):
    if len(str1) != len(str2):
        return False
    list_str1 = list(str1)
    for r in str2:
        if r in list_str1:
            list_str1.remove(r)
        else:
            return False
    return True


print(sravnenie("bebra", "ebayb"))
