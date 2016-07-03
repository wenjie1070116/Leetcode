class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0: return a
        A = (a&b)<<1
        B = a^b
        return self.getSum(A, B)
        