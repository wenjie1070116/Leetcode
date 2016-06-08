class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        for i in xrange(1, m):
            grid[i][0] += grid[i-1][0]
        for j in xrange(1, n):
            grid[0][j] += grid[0][j-1]
        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]