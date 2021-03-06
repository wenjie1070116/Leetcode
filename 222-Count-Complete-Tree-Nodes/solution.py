# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        level = 0
        nodes = [root]
        res = 0
        while True:
            level += 1
            new = []
            for node in nodes:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            if len(new) != 2**level:
                return 2**level-1+len(new)
            nodes = new
                    
        
    """
    # Time Limit Exceeded
    def maxdepth(self, root):
        if not root: return 0
        return max(self.maxdepth(root.left), self.maxdepth(root.right))+1
        
    def countNodes(self, root):
        if not root: return 0
        res = 0
        if self.maxdepth(root.left) == self.maxdepth(root.right):
            res += 2**(self.maxdepth(root.left))
            res += self.countNodes(root.right)
        else:
            res += 2**(self.maxdepth(root.right))
            res += self.countNodes(root.left)
        return res
    """
            