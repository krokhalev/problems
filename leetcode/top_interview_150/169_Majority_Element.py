class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        data = {}
        max_el = 0
        max_count = 0
        for n in nums:
            if n not in data:
                data[n] = 1
            else:
                data[n] += 1
                if data[n] > max_count:
                    max_count = data[n]
                    max_el = n

        return max_el


s = Solution()
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
