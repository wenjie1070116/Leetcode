class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]
            