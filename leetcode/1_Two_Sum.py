class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i + 1 < len(nums):
                    if nums[i] - target + nums[j] == 0:
                        return [i, j]


nums = [2, 7, 11, 15]
target = 9
s = Solution()

print(s.twoSum(nums, target))
