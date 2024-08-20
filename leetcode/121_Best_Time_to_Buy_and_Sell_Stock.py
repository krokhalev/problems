class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):

            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l += 1
                r = l + 1
                continue
            r += 1

        return res


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
