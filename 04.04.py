#coding=UTF-8
'''
解题思路：
递归。定义函数f(node)，该函数返回（当前节点下子树是否平衡，当前节点深度（从下至上））。
若node存在，则计算node.left、node.right各自的f()返回值。对node返回ansleft and ansright and abs(hleft - hright) <= 1，
即只有node左子树、右子树同时平衡，且左右子树深度差不大于1返回真。只要有任意一个条件不满足，则可以判断该树不平衡,返回假。
同时返回当node前最深子树深度+1，作为node本身的深度。
递归边界在叶子节点。叶节点必平衡，且深度为0.故返回（True，0）
'''

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def f(r):
            if r:
                ansleft, hleft = f(r.left)
                ansright, hright = f(r.right)
                return ansleft and ansright and abs(hleft - hright) <= 1, max(hleft, hright) + 1
            return True, 0
        return f(root)[0]