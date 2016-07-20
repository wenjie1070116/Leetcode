# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.root = root
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nodes or self.root:
            return True
        return False
        

    def next(self):
        """
        :rtype: int
        """
        while self.root:
            self.nodes.append(self.root)
            self.root = self.root.left
        self.root = self.nodes.pop()
        val = self.root.val
        self.root = self.root.right
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())