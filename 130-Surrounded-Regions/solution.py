class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        m, n = len(board), len(board[0])
        
        def change(x, y):
            board[x][y] = 'M'
            for dx, dy in zip((0, 1, 0 -1), (1, 0, -1, 0)):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == 'O':
                    change(nx, ny)
        
        for i in (0, m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    change(i, j)
        
        for j in (0, n):
            for i in xrange(1, m-1):
                if board[i][j] == 'O':
                    change(i, j)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'