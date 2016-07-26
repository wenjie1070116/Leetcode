class Solution(object):
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def valid(x, y, num):
            for i in xrange(9):
                if board[x][i] == str(num):
                    return False
            for j in xrange(9):
                if board[j][y] == str(num):
                    return False
            for i in xrange(x/3*3, x/3*3+3):
                for j in xrange(y/3*3, y/3*3+3):
                    if board[i][j] == str(num):
                        return False
            return True
                
        
        def dfs(x, y):
            if x >= 9:
                return True
            if y >= 9:
                return dfs(x+1, 0)
    
            if board[x][y] != '.':
                return dfs(x, y+1)
            else:
                for num in xrange(1, 10):
                    if valid(x,y,num):
                        board[x][y] = str(num)
                        if dfs(x,y+1):
                            return True
                        board[x][y] = '.'
            return False
        
        dfs(0, 0)