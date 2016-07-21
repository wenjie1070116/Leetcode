# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def valid(self, left, right, root):
        if not root: return True
        if root.val <= left or root.val >= right: return False
        return self.valid(left, root.val, root.left) and self.valid(root.val, right, root.right)
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        left, right = -sys.maxint, sys.maxint
        return self.valid(left, right, root)
        
        