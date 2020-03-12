# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            ans.append([])
            queue_tmp = []
            for node in queue:
                ans[-1].append(node.val)
                if node.left:
                    queue_tmp.append(node.left)
                if node.right:
                    queue_tmp.append(node.right)
            queue = queue_tmp
        return ans
