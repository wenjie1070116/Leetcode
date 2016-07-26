class Solution(object):
    def GCD(self, a, b):
        Max = max(a, b)
        Min = min(a, b)
        if Max%Min == 0: return Min
        return self.GCD(Max-Min, Min)
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        gcd = self.GCD(x, y)
        X = x/gcd
        Y = y/gcd
        range_min = min(X, Y, [Y-X,X-Y][X>Y])*gcd
        range_max = (X+Y)*gcd
        if range_min<=z<=range_max:
            return True
        return False
        
        