class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appear = set()
        while True:
            appear.add(n)
            new = 0
            while n:
                new += (n%10)**2
                n /= 10
            n = new
            if n == 1: return True
            if n in appear: return False
            