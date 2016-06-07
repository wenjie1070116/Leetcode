class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [i+1 for i in xrange(9)]
        def dfs(pos, temp, res):
            if len(temp) == k:
                if sum(temp) == n:
                    res.append([]+temp)
                return
            if sum(temp) > n:
                return 
            for i in xrange(pos, 10):
                temp.append(i)
                dfs(i+1, temp, res)
                temp.pop()
        res = []
        dfs(1, [], res)
        return res
        