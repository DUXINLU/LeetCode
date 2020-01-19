class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        return max(dp)
