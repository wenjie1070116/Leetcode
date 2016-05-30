# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isreverse(self, root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2 or root1.val != root2.val: return False
        return self.isreverse(root1.left, root2.right) and self.isreverse(root1.right, root2.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right): return True
        if not root.left or not root.right: return False
        return self.isreverse(root.left, root.right)
        