# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        def dfs(node, temp, res):
            if not node.left and not node.right:
                if sum(temp) == Sum:
                    res.append([]+temp) # take care that should append []+temp instead of temp
                return
            if node.left:
                temp.append(node.left.val)
                dfs(node.left, temp, res)
                temp.pop()
            if node.right:
                temp.append(node.right.val)
                dfs(node.right, temp, res)
                temp.pop()
        res = []
        dfs(root, [root.val], res)
        return res
        