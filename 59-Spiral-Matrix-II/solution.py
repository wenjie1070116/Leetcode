class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0: return []
        res = [[0]*n for _ in xrange(n)]
        i, j = 0, 0
        num = 1
        while num <= n*n:
            while j < n and res[i][j] == 0:
                res[i][j] = num
                num += 1
                j += 1
            j -= 1
            i += 1
            while i < n and res[i][j] == 0:
                res[i][j] = num
                num += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and res[i][j] == 0:
                res[i][j] = num
                num += 1
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and res[i][j] == 0:
                res[i][j] = num
                num += 1
                i -= 1
            i += 1
            j += 1
        return res