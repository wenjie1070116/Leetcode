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
        
        """
        for i in xrange(m):
            for j in xrange(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == 'O':
                    change(i, j)
        """
        change(0,0)
        change(0,2)
        change(2,0)
        change(2,2)
       
        print board
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'M':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'