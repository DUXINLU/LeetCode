# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def f(node):
            if not node:
                return 0
            left=f(node.left)
            if left==-1:
                return -1
            right=f(node.right)
            if right==-1:
                return -1
            if abs(right-left)<2:
                return max(left,right)+1
            return -1
        return f(root)!=-1