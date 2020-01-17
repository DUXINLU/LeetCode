# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def f(node,ans):
            if node.left:
                f(node.left,ans)
            ans.append(node.val)
            if node.right:
                f(node.right,ans)
            if (not node.left) and (not node.right):
                return
        ans=[]
        f(root,ans)
        return ans