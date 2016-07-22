class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        left = [False]*(2*n)
        right = [False]*(2*n)
        vertical = [False]*n
        def dfs(x, left, right, vertical, res):
            if x == n:
                res[0] += 1
                return
            for y in xrange(n):
                if not left[x-y] and not right[x+y] and not vertical[y]:
                    left[x-y] = True
                    right[x+y] = True
                    vertical[y] = True
                    dfs(x+1, left, right, vertical, res)
                    left[x-y] = False
                    right[x+y] = False
                    vertical[y] = False
        res = [0]
        dfs(0, left, right, vertical, res)
        return res[0]