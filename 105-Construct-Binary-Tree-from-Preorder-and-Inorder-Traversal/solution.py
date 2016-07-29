# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, preorder, s1, e1, inorder, s2, e2):
        if s1 > e1 or s2 > e2: return
        root = TreeNode(preorder[s1])
        idx = inorder.index(preorder[s1])
        root.left = self.build(preorder, s1+1, s1+idx, inorder, s2, idx-1)
        root.right = self.build(preorder, s1+idx+1, e1, inorder, idx+1, e2)
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) != len(inorder): return
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        