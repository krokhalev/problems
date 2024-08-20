class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1

        return sorted(map, key=map.get)[-k:]


nums = [1, 1, 1, 2, 2, 3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
