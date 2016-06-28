class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return 'invalid input'
        if n == 0: return 1
        if n == 1: return 10
        if n == 2: return 91
        res = [(0,0),(0,10),(9,81)]
        for i in xrange(3, n+1):
            dup = res[i-1][0]*10 + res[i-1][1]*(i-1)
            uni = 9*10**(i-1)-dup
            res.append((dup, uni))
        total = 0
        for i in xrange(1, n+1):
            total += res[i][1]
        return total
        