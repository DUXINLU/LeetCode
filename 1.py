from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # print(nums[i] + nums[j])
                if (nums[i] + nums[j]) == target:
                    return i, j


if __name__ == "__main__":
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
