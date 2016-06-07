class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        visited = [[0]*n for _ in xrange(m)]
        
        def dfs(x, y, visited, temp, res):
            mark = False
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny] > matrix[x][y]:
                    mark = True
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        dfs(nx, ny, visited, temp+1, res)
                        visited[nx][ny] = 0
                    else:
                        res[0] = max(res[0], temp+visited[nx][ny])
            if not mark:
                res[0] = max(res[0], temp)
                return
        
        res = [0]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j]:
                    dfs(i, j, visited, 1, res)
                    visited[i][j] = res[0]
                
        return res[0]
                    
                
        