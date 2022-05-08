class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for _ in range(len(nums)):
            if len(nums) == 1:
                return nums[0]
            elif nums[0] == nums[1]:
                del nums[0:2]
                if len(nums) == 1:
                    return nums[0]
            else:
                return nums[0]


nums_list = [4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums_list))
