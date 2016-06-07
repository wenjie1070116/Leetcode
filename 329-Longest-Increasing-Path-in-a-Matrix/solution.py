class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in xrange(m)]
        
        def dfs(i, j):
            for dx, dy in zip([0, -1, 0, 1],[-1,0,1,0]):
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj] < matrix[i][j]:
                    if not dp[ni][nj]: dp[ni][nj] = dfs(ni, nj)
                    dp[i][j] = max(dp[i][j], dp[ni][nj]+1)
            dp[i][j] = max(dp[i][j], 1)
            return dp[i][j]
        
        for i in xrange(m):
            for j in xrange(n):
                if not dp[i][j]:
                    dp[i][j] = dfs(i, j)
        return max([max(x) for x in dp])