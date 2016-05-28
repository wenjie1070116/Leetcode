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
        self.res = False
        def dfs(node, Sum):
            if not node.left and not node.right and Sum == sum:
                    self.res = True
            if node.left:
                dfs(node.left, Sum+node.left.val)
            if node.right:
                dfs(node.right, Sum+node.right.val)
        dfs(root, root.val)
        return self.res
                
        