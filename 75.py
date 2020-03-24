# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        reverse = 0
        queue = [root]
        ans = []
        while queue:
            queue_tmp = []
            for node in queue:
                if node.left:
                    queue_tmp.append(node.left)
                if node.right:
                    queue_tmp.append(node.right)
            if reverse:
                queue.reverse()
                ans.append([])
                for node in queue:
                    ans[-1].append(node.val)
            else:
                ans.append([])
                for node in queue:
                    ans[-1].append(node.val)
            reverse = 1 - reverse
            queue = queue_tmp
        return ans