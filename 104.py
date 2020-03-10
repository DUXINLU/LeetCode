# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans=0
        queue=[root]
        while queue:
            queue_tmp=[]
            for node in queue:
                if node.left:
                    queue_tmp.append(node.left)
                if node.right:
                    queue_tmp.append(node.right)
            queue=queue_tmp
            ans+=1
        return ans
