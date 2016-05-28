class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        X = x
        y = 0
        while X:
            y = y*10+X%10
            X /= 10
        return x == y