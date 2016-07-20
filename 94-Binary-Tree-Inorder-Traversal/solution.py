# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        nodes = []
        while nodes or root:
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            res.append(root.val)
            root = root.right
        return res
        