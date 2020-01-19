class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_ = 99999
        for i in range(len(prices)):
            min_ = min(prices[i], min_)
            ans = max(ans, prices[i] - min_)
        return ans
