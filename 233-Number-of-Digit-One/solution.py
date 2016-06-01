class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        res = 0
        N = n
        idx = 0
        while n:
            cur = n%10
            n /= 10
            if cur < 1:
                res += n*10**idx
            elif cur == 1:
                res += n*10**idx+N%(10**idx)+1
            else:
                res += (n+1)*10**idx
            idx += 1
        return res
                