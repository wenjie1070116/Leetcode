class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        reverse = True if n < 0 else False
        n = abs(n)
        sign = -1 if x < 0 and abs(n)%2 == 1 else 1
        res = self.myPow(x, n/2)**2*[x,1][n%2==0]
        if reverse:
            return 1/(sign*res)
        return sign*res