# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        left_tail = left
        while left_tail.right:
            left_tail = left_tail.right
        left_tail.right = right
        root.right = left
        root.left = None
        return root
        