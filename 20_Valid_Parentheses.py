class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for p in s:
            if p in map:
                stack.append(map[p])
            else:
                if len(stack) == 0 or stack.pop(-1) != p:
                    return False

        if len(stack) != 0:
            return False

        return True


s = Solution()
print(s.isValid("()"))
