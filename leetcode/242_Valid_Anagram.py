class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
