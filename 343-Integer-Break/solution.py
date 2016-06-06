class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        dp = [0]*(n+1)
        dp[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i/2+1):
                dp[i] = max(dp[i], j*dp[i-j], dp[j]*(i-j), j*(i-j), dp[j]*dp[i-j]) # not just dp[j]*dp[i-j]
        return dp[n]