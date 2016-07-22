class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n <= 0: return []
        board = [['.']*n for i in xrange(n)]
        left = [False]*(2*n)
        right = [False]*(2*n)
        vertical = [False]*n
        def dfs(board, left, right, vertical, x, res):
            if x == n:
                temp = []
                for row in board:
                    temp.append(''.join(row))
                res.append(temp)
                return
            for y in xrange(n):
                if not left[x-y] and not right[x+y] and not vertical[y]:
                    board[x][y] = 'Q'
                    left[x-y] = True
                    right[x+y] = True
                    vertical[y] = True
                    dfs(board, left, right, vertical, x+1, res)
                    board[x][y] = '.'
                    left[x-y] = False
                    right[x+y] = False
                    vertical[y] = False
        res = []
        dfs(board, left, right, vertical, 0, res)
        return res