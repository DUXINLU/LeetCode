class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        max1 = max(nums)
        index_max1 = nums.index(max1)
        nums.pop(index_max1)
        max2 = max(nums)
        if max1 >= max2 * 2:
            return index_max1
        return -1
