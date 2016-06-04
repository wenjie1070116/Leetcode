class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        res = []
        count = 1
        while count <= m*n:
            while j < n and matrix[i][j] != 0:
                res.append(matrix[i][j])
                matrix[i][j] = 0
                j += 1
                count += 1
            j -= 1
            i += 1
            while i < m and matrix[i][j] != 0:
                res.append(matrix[i][j])
                matrix[i][j] = 0
                i += 1
                count += 1
            i -= 1
            j -= 1
            while j >= 0 and matrix[i][j] != 0:
                res.append(matrix[i][j])
                matrix[i][j] = 0
                j -= 1
                count += 1
            j += 1
            i -= 1
            while i >= 0 and matrix[i][j] != 0:
                res.append(matrix[i][j])
                matrix[i][j] = 0
                i -= 1
                count += 1
            i += 1
            j += 1
        return res