# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        def dfs(node, temp, res):
            if not node.left and not node.right:
                res.append('->'.join(temp))
                return
            if node.left:
                temp.append(str(node.left.val))
                dfs(node.left, temp, res)
                temp.pop()
            if node.right:
                temp.append(str(node.right.val))
                dfs(node.right, temp, res)
                temp.pop()
        res = []
        dfs(root, [str(root.val)], res)
        return res