class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1: return []
        res = [[1]]
        for i in xrange(1, numRows):
            cur = []
            for j in xrange(i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(res[-1][j-1]+res[-1][j])
            res.append(cur)
        return res
        