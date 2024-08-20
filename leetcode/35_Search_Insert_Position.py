class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if target < nums[i]:
                return i
            if i == len(nums) - 1 and target > nums[i]:
                return i + 1


nums = [1, 3, 5, 6]
target = 7
s = Solution()
print(s.searchInsert(nums, target))
