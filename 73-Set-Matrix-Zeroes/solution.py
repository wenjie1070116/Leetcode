class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        m, n = len(matrix), len(matrix[0])
        firstrow = False
        firstcol = False
        for i in xrange(m):
            if matrix[i][0] == 0:
                firstcol = True
                break
        for j in xrange(n):
            if matrix[0][j] == 0:
                firstrow = True
                break
        for i in xrange(1, m):
            for j in xrange(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0]*n
        for j in xrange(1, n):
            if matrix[0][j] == 0:
                for i in xrange(1, n):
                    matrix[i][j] = 0
        if firstrow:
            matrix[0] = [0]*n
        if firstcol:
            for i in xrange(m):
                matrix[i][0] = 0