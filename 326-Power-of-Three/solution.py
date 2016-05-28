import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        idx = round(math.log(n, 3))
        if 3**idx == n:
            return True
        return False
        '''
        # another method
        return n > 0 && 1162261467 % n == 0;
        '''
        