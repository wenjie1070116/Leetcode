# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        def dfs(node, Sum):
            if not node.left and not node.right and Sum == sum:
                    return True
            if node.left and dfs(node.left, Sum+node.left.val):
                return True
            if node.right and dfs(node.right, Sum+node.right.val):
                return True
        if dfs(root, root.val): return True
        return False        
        