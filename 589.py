"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def f(node,ans):
            print(node.val)
            ans.append(node.val)
            if not node.children:
                return
            for i in node.children:
                f(i,ans)
        ans=[]
        f(root,ans)
        return ans
