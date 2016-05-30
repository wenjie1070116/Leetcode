class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        f = [[False]*(m+1) for i in range(n+1)]
        f[0][0] = True

        for i in range(1, n+1):
            for j in range(1, m+1):
                f[i][j] = (
                    (f[i-1][j-1] and
                    (s[i-1] == p[j-1] or p[j-1] == '?' or p[j-1] == '*')) or
                    f[i-1][j] and p[j-1] == '*')

        return f[n][m]
        '''
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
                if s[i] == p[j] or p[j] == '?' or p[j] == '*':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    dp[i+1][j+1] = dp[i][j+1]
        return dp[-1][-1]
        '''