class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(num, temp, res):
            if len(temp) == k:
                res.append([]+temp)
                return
            for i in xrange(num, n+1):
                temp.append(i)
                dfs(i+1, temp, res)
                temp.pop()
        res = []
        dfs(1, [], res)
        return res