class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        cur = 1
        dp = [sys.maxint]*(n+1)
        dp[0] = 0
        for i in xrange(1, n+1):
            if i == cur**2:
                dp[i] = 1
                cur += 1
            else:
                for num in range(cur-1, 0, -1):
                    dp[i] = min(dp[i], dp[i-num**2]+1)
        return dp[n]