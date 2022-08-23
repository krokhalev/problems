class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_shift = 0
        right_shift = 0
        s_arr = list(s)
        for index in range(len(s_arr)):
            if left_shift >= len(s_arr) - 1 - right_shift:
                return "".join(s_arr)

            if s_arr[left_shift].isalpha() and s_arr[len(s_arr) - 1 - right_shift].isalpha():
                left, right = s_arr[left_shift], s_arr[len(s_arr) - 1 - right_shift]
                s_arr[len(s_arr) - 1 - right_shift], s_arr[left_shift] = left, right
                left_shift += 1
                right_shift += 1

            elif not s_arr[left_shift].isalpha() and not s_arr[len(s_arr) - 1 - right_shift].isalpha():
                left_shift += 1
                right_shift += 1

            elif s_arr[left_shift].isalpha() and not s_arr[len(s_arr) - 1 - right_shift].isalpha():
                right_shift += 1

            elif not s_arr[left_shift].isalpha() and s_arr[len(s_arr) - 1 - right_shift].isalpha():
                left_shift += 1


sol = Solution()
print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
