class Solution(object):
    def isValid(self, s):
        store = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for r in s:
            if r in store:
                stack.append(store[r])
            else:
                if len(stack) == 0 or stack.pop(-1) != r:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True


s = Solution()
print(s.isValid("([{((}])"))
