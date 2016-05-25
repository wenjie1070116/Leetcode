class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return
        n = len(matrix)
        for i in xrange(n-1):
            for j in xrange(n-1-i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
        start, end = 0, n-1
        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1