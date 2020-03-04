class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r_ = len(nums)
        c_ = len(nums[0])
        if r_ * c_ != r * c:
            return nums

        _ = []
        for i in nums:
            _ += i

        ans = []

        for i in range(r):
            ans.append([])
            for j in range(c):
                ans[i].append(_[i * c + j])

        return ans
