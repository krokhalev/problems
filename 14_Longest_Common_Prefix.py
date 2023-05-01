class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        map = {}
        brk = False
        if len(strs) == 1:
            return strs[0]
        for indexL, l in enumerate(strs[0]):
            if brk:
                break
            for indexS, st in enumerate(strs[1:]):
                if indexL < len(st) and st[indexL] == l:
                    if indexL in map and map[indexL] != l:
                        res += l
                        map[indexL] = l
                    elif indexL not in map:
                        res += l
                        map[indexL] = l
                else:
                    res = res[:indexL]
                    brk = True
                    break

        return res


strs = ["aaa","aa","aaa"]
s = Solution()
print(s.longestCommonPrefix(strs))
