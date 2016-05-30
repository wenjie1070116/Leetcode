class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check row
        for i in xrange(9):
            check = set()
            for j in xrange(9):
                if board[i][j] in check: return False
                elif board[i][j] != '.':
                    check.add(board[i][j])
        # check column
        for j in xrange(9):
            check = set()
            for i in xrange(9):
                if board[i][j] in check: return False
                elif board[i][j] != '.':
                    check.add(board[i][j])
        # check diagnol
        for n in xrange(9):
            check = set()
            for i in xrange(3):
                for j in xrange(3):
                    if board[n/3*3+i][n%3*3+j] in check: return False
                    elif board[n/3*3+i][n%3*3+j] != '.':
                        check.add(board[n/3*3+i][n%3*3+j])
        return True