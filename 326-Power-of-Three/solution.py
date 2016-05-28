class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0: return False
        idx = int(math.log(n, 3))
        if 3^idx == n:
            return True
        return False
        