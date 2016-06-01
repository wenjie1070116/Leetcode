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
        if d < r: return 0
        temp = r
        res = 1
        while (temp << 1) <= d:
            temp <<= 1
            res <<= 1
        d -= temp
        temp >>= 1
        idx = res
        while d >= r:
            idx >>= 1
            if d >= temp:
                res |= idx
                d -= temp
            temp >>= 1
        if sign*res > 2**31-1: return 2**31-1
        if sign*res < -2**31: return -2**31
        return sign*res
        
            
            
        
                
                
        