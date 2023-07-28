class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        len_nums = len(nums)
        tmp = 0
        use_tmp = False
        res = 0
        for i in range(len_nums):
            if i == 0:
                continue
            elif i == len_nums - 1:
                continue
            elif nums[i - 1] < nums[i] > nums[i + 1]:
                res += 1
            elif nums[i - 1] > nums[i] < nums[i + 1]:
                res += 1
            elif nums[i - 1] == nums[i] == nums[i + 1]:
                continue
            elif nums[i] == nums[i + 1]:
                tmp = nums[i - 1]
                use_tmp = True
            elif nums[i - 1] == nums[i] != nums[i + 1] and use_tmp:
                if tmp < nums[i] > nums[i + 1]:
                    res += 1
                elif tmp > nums[i] < nums[i + 1]:
                    res += 1

        return res


s = Solution()
print(s.countHillValley(nums=[6, 6, 5, 5, 4, 1]))
