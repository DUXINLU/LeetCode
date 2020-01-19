class Solution:
    def climbStairs(self, n: int) -> int:
        ans_list=[1,2]
        for i in range(2,n):
            ans_list.append(ans_list[i-1]+ans_list[i-2])
        return ans_list[n-1]