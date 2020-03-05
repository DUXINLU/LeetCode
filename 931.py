#coding=UTF-8
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m,n=len(A),len(A[0])
        dp=[[101]*(n+2) for i in range(m)]
        for i in range(n):
            dp[0][i+1]=A[0][i]
        for i in range(1,m):
            for j in range(1,n+1):
                dp[i][j]=A[i][j-1]+min(dp[i-1][j-1:j+2])
        return min(dp[-1])

'''
官方解答：
class Solution(object):
    def minFallingPathSum(self, A):
        while len(A) >= 2:
            row = A.pop()            
            for i in xrange(len(row)):
            #这句话的边界判断写的很好  下标左边最大值右边最小值
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])
'''