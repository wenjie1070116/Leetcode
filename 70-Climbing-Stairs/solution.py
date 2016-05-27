class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dp = [1]*(n+1)
        for i in xrange(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]