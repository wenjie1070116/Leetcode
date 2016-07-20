# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [0, 0]
            left_Max, left_ign = dfs(root.left)
            right_Max, right_ign = dfs(root.right)
            return  [max(root.val+left_ign+right_ign, left_Max+right_Max), left_Max+right_Max]
        return dfs(root)[0]
        
        