class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        candidates.sort()
        def dfs(pos, temp, res):
            if sum(temp) == target:
                res.append([]+temp)
                return
            if sum(temp) > target:
                return
            for i in xrange(pos, len(candidates)):
                temp.append(candidates[i])
                dfs(i, temp, res)
                temp.pop()
        res = []
        dfs(0, [], res)
        return res
        