import bisect
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        candidates.sort()
        self.idx = bisect.bisect_right(candidates, target)
        def dfs(pos, temp, res):
            if sum(temp) == target:
                res.append([]+temp)
                return
            if sum(temp) > target:
                return
            for i in xrange(pos, self.idx):
                if i != pos and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                dfs(i+1, temp, res)
                temp.pop()
        res = []
        dfs(0, [], res)
        return res
        