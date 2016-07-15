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
            for dx, dy in zip((0, 1, 0, -1), (1, 0, -1, 0)):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] == 'O':
                    board[nx][ny] = 'M'
                    change(nx, ny)
        
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'M'
            if board[i][n-1] == 'O':
                board[i][n-1] = 'M'
            
        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'M'
            if board[m-1][j] == 'O':
                board[m-1][j] = 'M'
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'M':
                    change(i, j)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'