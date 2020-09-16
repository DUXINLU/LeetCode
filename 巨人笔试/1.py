#
# return an array including the max of sliding window
# @param arr int整型一维数组 the arr
# @param w int整型 the window size
# @return int整型一维数组
#
class Solution:
    def slidingwindowMax(self, arr, w):
        ans = []
        for i in range(len(arr) - w + 1):
            ans.append(max(arr[i:i + w]))
        return ans


s = Solution()
print(s.slidingwindowMax([4, 3, 5, 4, 3, 3, 6, 7], 3))
