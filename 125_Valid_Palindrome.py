class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for r in s.lower():
            if r.isdigit() or r.isalpha():
                res += r
            else:
                continue

        if len(res) % 2 != 0:
            left = res[(len(res)//2)+1:]
            right = res[:len(res)//2][::-1]
            if left == right:
                return True
        else:
            left = res[len(res)//2:]
            right = res[:len(res)//2][::-1]
            if left == right:
                return True

        return False


s = Solution()
print(s.isPalindrome("race a car"))
