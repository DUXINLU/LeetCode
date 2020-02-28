#coding=UTF-8
'''
解题思路：
这个三指针是咋回事？没太想得很明白
'''

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        ans=[1]
        n3,n5,n7=0,0,0
        for i in range(k):
            ans.append(min(ans[n3]*3,ans[n5]*5,ans[n7]*7))
            if ans[-1]==ans[n3]*3:
                n3+=1
            if ans[-1]==ans[n5]*5:
                n5+=1
            if ans[-1]==ans[n7]*7:
                n7+=1
        return ans[k-1]