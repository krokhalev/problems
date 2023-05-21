class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        next = 0
        res = 0
        while next < len(s):
            biggest = 0
            tmp = 0
            arr = []
            for st in s[next:]:
                if st not in arr:
                    arr.append(st)
                    tmp += 1
                else:
                    arr = []
                    tmp = 0
                biggest = max(biggest, tmp)

            res = max(res, biggest)
            next += 1
        return res


s = Solution()
print(s.lengthOfLongestSubstring("jbpnbwwd"))
