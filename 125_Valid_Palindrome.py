class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for r in s.lower():
            if r.isdigit() or r.isalpha():
                res += r
            else:
                continue

        if len(res) in [0, 1]:
            return True

        if len(res) % 2 == 0:
            for i in range(len(res)):
                if res[i] != res[-i - 1]:
                    return False
                if i == (len(res) / 2) - 1:
                    return True
        else:
            for i in range(len(res)):
                if res[i] != res[-i - 1]:
                    return False
                if i == ((len(res) - 1) / 2) - 1:
                    return True

        return False


s = Solution()
print(s.isPalindrome("."))
