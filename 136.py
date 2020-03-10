class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:]:
                nums[nums[i+1:].index(nums[i])+i+1],nums[i]=0,0
        return sum(nums)