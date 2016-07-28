# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def generate(self, nums):
        if not nums: return [None]
        res = []
        for idx in xrange(len(nums)):
            left = self.generate(nums[:idx])
            right = self.generate(nums[idx+1:])
            for l in left:
                for r in right:
                    root = TreeNode(nums[idx])
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
                    
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0: return []
        nums = [i for i in xrange(1, n+1)]
        return self.generate(nums)
            
        
        