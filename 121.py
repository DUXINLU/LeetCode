class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_=99999
        ans=0
        for i in prices:
            if i<min_:
                min_=i
            if i-min_>ans:
                ans=i-min_
        return ans