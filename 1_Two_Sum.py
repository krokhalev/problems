class Solution(object):
    def twoSum(self, nums, target):
        store = {}
        for i in range(len(nums)):
            print(store)
            sec = target - nums[i]
            print(sec)
            if sec not in store:
                store[nums[i]] = i
            else:
                return [store[sec], i]


s = Solution()
print(s.twoSum([2, 15, 11, 7], 9))
