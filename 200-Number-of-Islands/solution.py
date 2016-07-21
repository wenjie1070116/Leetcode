class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        
        def change(x, y):
            grid[x][y] = '0'
            for dx, dy in zip((0,1,0,-1),(1,0,-1,0)):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
                    change(nx,ny)
        
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    res += 1
                    change(i,j)
        return res
        