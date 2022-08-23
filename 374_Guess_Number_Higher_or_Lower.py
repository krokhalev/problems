# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num):
    pick = 50
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            answer = guess(mid)
            if answer == 0:
                return mid
            elif answer == 1:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
print(s.guessNumber(1000))
