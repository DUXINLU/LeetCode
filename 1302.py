# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def f(root):
            queue=[]
            queue_temp=[]
            queue.append(root)
            #max_depth=0
            ans=0
            while queue:
                ans=0
                for node in queue:
                    ans+=node.val
                    if node.left:
                        queue_temp.append(node.left)
                    if node.right:
                        queue_temp.append(node.right)
                queue=queue_temp
                queue_temp=[]
            return ans
        return f(root)
