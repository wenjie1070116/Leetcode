class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        nums.sort()
        
        def dfs(pos, temp, res):
            res.append([]+temp)
            for i in xrange(pos, len(nums)):
                if i != pos and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(i+1, temp, res)
                temp.pop()
        
        res = []
        dfs(0, [], res)
        return res
        