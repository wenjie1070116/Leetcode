# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        idx = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            idx += 1
            if idx == k:
                return root.val
            root = root.right