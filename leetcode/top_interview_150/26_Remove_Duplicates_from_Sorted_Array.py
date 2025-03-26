class Solution:
    def removeDuplicates(self, nums):
        k = 0
        data = {}
        for i in range(len(nums)):
            if nums[i] not in data:
                nums[k] = nums[i]
                data[nums[i]] = ""
                k += 1
        return k


s = Solution()
print(s.removeDuplicates(nums=[1, 1, 2]))
