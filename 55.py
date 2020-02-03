class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max=0
        for i in range(len(nums)):
            if i<=current_max:
                if i+nums[i]>current_max:
                    current_max=i+nums[i]
        return current_max+1>=len(nums)