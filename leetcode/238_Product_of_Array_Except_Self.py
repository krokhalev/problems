class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []
        brk = 0
        while brk < len(nums):
            tmp = 0
            for num in nums[:brk]+nums[brk+1:]:
                if num == 0:
                    tmp = 0
                    break
                if tmp == 0:
                    tmp += num
                    continue
                tmp *= num
            res.append(tmp)
            brk += 1

        return res


s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
