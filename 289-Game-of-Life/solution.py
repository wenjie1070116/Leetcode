class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        for i in xrange(m):
            for j in xrange(n):
                cur = board[i][j]
                for dx, dy in zip((-1,0,0,-1,-1,1,1,1),(-1,-1,1,0,1,0,-1,1)):
                    nx, ny = i+dx, j+dy
                    if 0<=nx<m and 0<=ny<n:
                        if board[nx][ny] == 1 or board[nx][ny] == 2:
                            cur += 1
                if cur == 3 and board[i][j] == 0:
                    board[i][j] = 4
                elif cur == 3 or cur == 4 and board[i][j] == 1:
                    board[i][j] = 1
                elif board[i][j] == 1:
                    board[i][j] = 2
                else:
                    board[i][j] = 0
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 4:
                    board[i][j] = 1
                if board[i][j] == 2:
                    board[i][j] = 0