class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        if letter not in s:
            return 0

        count = 0
        for st in s:
            if st == letter:
                count += 1

        return int(count / len(s) * 100)


s = Solution()
print(s.percentageLetter(s="jjjj", letter="k"))
