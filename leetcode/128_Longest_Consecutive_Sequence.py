class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        updatedNums = sorted(set(nums))
        heap = [updatedNums[0]]
        res = 1
        tmpRes = []
        for num in updatedNums[1:]:
            if num not in heap and num - 1 in heap:
                heap.append(num)
                res += 1
            else:
                tmpRes.append(res)
                res = 1
                heap = [num]

        if len(tmpRes) != 0 and len(heap) > sorted(tmpRes)[-1]:
            return len(heap)

        if len(tmpRes) == 0:
            return res

        return sorted(tmpRes)[-1]


s = Solution()
print(s.longestConsecutive([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]))
