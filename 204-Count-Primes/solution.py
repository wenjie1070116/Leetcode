import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        dp = [1]*n
        dp[0] = 0
        dp[1] = 0
        res = 0
        for i in xrange(2, n):
            if dp[i] == 1:
                idx = 2
                while i*idx < n:
                    dp[i*idx] = 0
                    idx += 1
        return sum(dp)
        
        '''
        # TLE
        if n < 2: return 0
        primes = [2]
        for i in xrange(3, n):
            mark = True
            for prime in primes:
                if prime > math.sqrt(n):
                    break
                if i%prime == 0:
                    mark = False
                    break
            if mark:
                primes.append(i)
        return len(primes)
        '''
        