class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        nums.sort()
        def dfs(nums, pos, temp, res):
            res.append([]+temp)
            for i in xrange(pos, len(nums)):
                temp.append(nums[i])
                dfs(nums, i+1, temp, res)
                temp.pop()
        
        res = []
        dfs(nums, 0, [], res)
        return res
        