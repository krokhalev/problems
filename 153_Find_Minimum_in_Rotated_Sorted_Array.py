class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


s = Solution()
print(s.findMin([6, 8, 9, 10, 1, 2, 4, 5]))
