import time

class Solution:
    def climbStairs(self, n: int) -> int:  # dynamic programming
        one, two = 1, 1
        time.sleep(0.1)

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one

# time out solution
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def countSteps(n):
#             if n == 1:
#                 return 1
#             if n == 2:
#                 return 2
#             return countSteps(n-1) + countSteps(n-2)
#
#         return countSteps(n)


s = Solution()
print(s.climbStairs(5))
