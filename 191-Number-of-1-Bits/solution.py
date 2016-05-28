class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            if n&1 == 1:
                res += 1
            n >>= 1
        return res