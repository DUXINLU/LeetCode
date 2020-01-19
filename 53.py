class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp=[nums[0],]
        for i in range(1,len(nums)):
            dp.append(max(nums[i]+dp[i-1],nums[i]))
        return max(dp)