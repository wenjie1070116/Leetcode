# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        nodes = [root]
        res = [[root.val]]
        idx = 0
        while nodes:
            new = []
            temp = []
            for node in nodes:
                if node.left:
                    new.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    new.append(node.right)
                    temp.append(node.right.val)
            nodes = new
            if temp:
                if idx%2 == 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)
            idx += 1
        return res
                
        