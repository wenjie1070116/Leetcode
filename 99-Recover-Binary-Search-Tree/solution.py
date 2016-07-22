# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.first = None
        self.second = None
        def dfs(root):
            if root.left and root.val < root.left.val:
                if not self.first:
                    self.first = root.left
                else:
                    self.second = root
                    return
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        if self.first and self.right:
            temp = self.first.val
            self.first.val = self.second.val
            self.second.val = temp
        return
            
        