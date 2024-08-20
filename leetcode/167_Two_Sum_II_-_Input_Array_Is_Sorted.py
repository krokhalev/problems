class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            numSum = numbers[left] + numbers[right]

            if numSum > target:
                right -= 1
            elif numSum < target:
                left += 1
            else:
                return [left + 1, right + 1]


s = Solution()
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
