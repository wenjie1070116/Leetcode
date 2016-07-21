class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if not board: return False
        
        def dfs(x,y,pos):
            if pos == len(word)-1:
                return True
            for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] = word[pos+1] and dfs(nx, ny, pos+1):
                    return True
            return False
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
        