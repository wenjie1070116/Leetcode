class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            res = (res<<1)|(n&1)
            n >>= 1
        return res