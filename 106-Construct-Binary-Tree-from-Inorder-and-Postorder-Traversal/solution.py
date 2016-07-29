# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self, postorder, s1, e1, inorder, s2, e2):
        if s1 > e1 or s2 > e2: return
        root = TreeNode(postorder[e1])
        idx = inorder.index(postorder[e1])
        root.left = self.build(postorder, s1, s1+(idx-s2)-1, inorder, s2, idx-1)
        root.right = self.build(postorder, s1+idx-s2, e1-1, inorder, idx+1, e2)
        return root
    
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder or len(inorder) != len(postorder):
            return
        return self.build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)
        
        