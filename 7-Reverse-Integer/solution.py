class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x:
            res = res*10 + x%10
            x /= 10
        if sign*res > 2**31-1 or sign*res < -2**31: return 0
        return sign*res