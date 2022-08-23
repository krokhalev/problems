class Solution(object):
    def singleNumber(self, nums):
        xor_arr = 0
        for i in range(len(nums)):
            xor_arr = xor_arr ^ nums[i]
        return xor_arr


s = Solution()
print(s.singleNumber([2,2,1]))
