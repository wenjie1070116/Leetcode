class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        
        def dfs(visited, temp, res):
            if len(temp) == len(nums):
                res.append([]+temp)
                return
            for i in xrange(nums):
                if i != 1 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                temp.append(nums[i])
                visited.add(i)
                dfs(visited, temp, res)
                temp.pop()
                visited.remove(i)
        
        visited = set()
        res = []
        dfs(visited, [], res)
        return res
        