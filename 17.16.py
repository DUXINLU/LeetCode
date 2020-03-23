class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)

        dp=[nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))
        return dp[-1]