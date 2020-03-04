#coding=UTF-8
'''
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数
'''
class Solution:
    def isUgly(self, num: int) -> bool:
        dp=[1]
        n2,n3,n5=0,0,0
        while dp[-1]<num:
            dp.append(min(dp[n2]*2,dp[n3]*3,dp[n5]*5))
            if dp[-1]==dp[n2]*2:
                n2+=1
            if dp[-1]==dp[n3]*3:
                n3+=1
            if dp[-1]==dp[n5]*5:
                n5+=1
        if dp[-1]==num:
            return True
        return False
'''
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        root_val=root.val
        ans=True
        queue=[root]
        queue_temp=[]
        while queue:
            for i in queue:
                if i.left:
                    queue_temp.append(i.left)
                if i.right:
                    queue_temp.append(i.right)
                if i.val!=root_val:
                    ans=False
            queue=queue_temp
            queue_temp=[]
        return ans
'''
给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：

它是一个空字符串，或者
它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
它可以被写作 (A)，其中 A 是有效字符串。
给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。
'''


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S:
            return 0

        stack = []
        for i in S:
            if i == '(':
                stack.append(i)
            if i == ')':
                if stack == [] or stack[-1] != '(':
                    stack.append(i)
                else:
                    stack = stack[:-1]
            print(stack)
        return len(stack)