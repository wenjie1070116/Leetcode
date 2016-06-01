class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return
        sign = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0: sign = -1
        d, r = abs(dividend), abs(divisor)
        if r == 1: return sign*d
        res = 0
        while d >= r:
            temp = r
            idx = 1
            while (temp << 1) <= r:
                temp <<= 1
                idx <<= 1
            d = d-temp
            res += idx
        return sign*res
                
                
        