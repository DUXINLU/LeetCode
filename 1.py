from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        nums_len = len(nums)
        for i in range(nums_len):
            dif = target - nums[i]
            if dif in nums_hash: 
                return [nums_hash[dif], i]
            nums_hash[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
