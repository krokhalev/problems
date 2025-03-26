class Solution:
    def removeDuplicates(self, nums):
        k = 0
        data = {}
        for i in range(len(nums)):
            if nums[i] not in data:
                data[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
            else:
                if data[nums[i]] < 2:
                    data[nums[i]] += 1
                    nums[k] = nums[i]
                    k += 1

        return k


s = Solution()
print(s.removeDuplicates(nums = [1,1,1,2,2,3]))
