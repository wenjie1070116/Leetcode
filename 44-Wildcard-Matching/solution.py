class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        if not p:
            return False
        dp = [[False]*(len(p)+1) for _ in xrange(len(s)+1)]
        dp[0][0] = True
        if p[0] == '*':
            dp[0][1] = True
        for i in xrange(len(s)):
            for j in xrange(len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
        return dp[-1][-1]