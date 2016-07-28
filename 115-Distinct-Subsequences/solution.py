class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t: return 1
        if not s or len(s) < len(t): return 0
        dp = [[0]*(len(t)+1) for _ in xrange(len(s)+1)]
        for i in xrange(len(s)+1):
            dp[i][0] = 1
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(t)+1):
                if i < j: dp[i][j] = 0
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        