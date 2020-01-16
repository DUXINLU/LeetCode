from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_s = 0
        while j > i:
            s = min(height[i], height[j]) * (j - i)
            print(height[i], height[j], i, j, s)
            if s > max_s:
                max_s = s
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_s


if __name__ == '__main__':
    s = Solution()
    s.maxArea([2, 3, 4, 5, 18, 17, 6])
