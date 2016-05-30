# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not root.left: return right + 1
        if not root.right: return left + 1
        return min(left, right)+1