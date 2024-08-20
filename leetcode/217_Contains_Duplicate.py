class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
