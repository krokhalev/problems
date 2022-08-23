class Solution(object):
    def searchMatrix(self, matrix, target):
        for s in matrix:
            if s[0] <= target <= s[-1]:
                left = 0
                right = len(s) - 1

                while left <= right:
                    mid = (left + right) // 2
                    if s[mid] == target:
                        return True
                    elif s[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
