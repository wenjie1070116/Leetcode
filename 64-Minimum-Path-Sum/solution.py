class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        for i in xrange(1, m):
            dp[i][0] += dp[i-1][0]
        for j in xrange(1, n):
            dp[0][j] += dp[0][j-1]
        for i in xrange(1, m):
            for j in xrange(1, m):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        