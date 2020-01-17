# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def f(node, ans):
            ans.append(node.val)
            if (not node.left) and (not node.right):
                return
            if node.left:
                f(node.left, ans)
            if node.right:
                f(node.right, ans)

        ans = []
        f(root, ans)
        return ans
