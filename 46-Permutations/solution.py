class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        
        def dfs(visited, temp, res):
            if len(temp) == len(nums):
                res.append([]+temp)
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    temp.append(num)
                    dfs(visited, temp, res)
                    visited.remove(num)
                    temp.pop()
        
        visited = set()
        res = []
        dfs(visited, [], res)
        return res
        