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
        self.last = TreeNode(-sys.maxint)
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.first and root.val < self.last.val:
            self.first = self.last
        if self.first and root.val < self.last.val:
            self.second = root
        self.last = root
        self.inorder(root.right)
        
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
        
        