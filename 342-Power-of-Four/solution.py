class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num&(num-1) != 0:
            return False
        count = 1
        while num&1 != 1:
            count += 1
            num >>= 1
        return count%2 == 1
        