class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        toCheck = sorted(s1)
        lenToCheck = len(toCheck)
        for i in range(len(s2) - lenToCheck + 1):
            if sorted(s2[i:i + lenToCheck]) == toCheck:
                return True

        return False


s = Solution()
print(s.checkInclusion("hello", "ooolleoooleh"))
