class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        count = 0
        res = []
        for i in range(len(nums)):
            if i == 0:
                count += 1
                continue

            if nums[i - 1] < nums[i]:
                count += 1
            else:
                res.append(count)
                count = 1

            if i == len(nums) - 1:
                res.append(count)

        return max(res)


s = Solution()
print(s.findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))
