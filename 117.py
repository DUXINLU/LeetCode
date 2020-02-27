"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue=[root]
        queue_temp=[]

        while queue:
            for i in range(len(queue)):
                if i<len(queue)-1:
                    queue[i].next=queue[i+1]
                if queue[i].left:
                    queue_temp.append(queue[i].left)
                if queue[i].right:
                    queue_temp.append(queue[i].right)
            queue=queue_temp
            queue_temp=[]
        return root