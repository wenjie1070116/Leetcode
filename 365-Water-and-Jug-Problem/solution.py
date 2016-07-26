class Solution(object):
    def GCD(self, a, b):
        while a%b != 0:
            temp = a-b
            a = max(temp, b)
            b = min(temp, b)
        return b
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0: return True
        if x == 0: return y==z
        if y == 0: return x==z
        gcd = self.GCD(x, y) if x > y else self.GCD(y, x)
        if z%gcd != 0: return False
        z /= gcd
        x /= gcd
        y /= gcd
        if 0<=z<=x+y:
            return True
        return False
        
        