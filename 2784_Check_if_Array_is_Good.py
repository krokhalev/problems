class Solution:
    def isGood(self, nums: list[int]) -> bool:
        max_num = max(nums)
        res = []
        for i in range(1, max_num + 1):
            res.append(i)

        res.append(max_num)

        return sorted(nums) == res


s = Solution()
print(s.isGood(nums=[2, 1, 3, 3]))
