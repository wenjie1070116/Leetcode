class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0]*(num+1)
        idx = 0
        for i in xrange(1, num+1):
            if i == 2**idx:
                bits[i] = 1
                idx += 1
            else:
                bits[i] = 1+bits[i-2**(idx-1)]
        return bits
        