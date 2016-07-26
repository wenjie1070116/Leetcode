# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
    
    def inorder(self, root):
        if not root:
            return
        left = self.inorder(root.left)
        if left.val > root.val:
            if not self.first:
                self.first = left
            elif not self.second:
                self.second = root
        right = self.inorder(root.right)
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        self.inorder(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        return
        
        