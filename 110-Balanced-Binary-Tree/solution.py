# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxdepth(self, root):
        if not root: return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        if abs(left-right) > 1 or left == -1 or right == -1: return -1
        else: return max(left, right)+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxdepth(root) != -1
        
        