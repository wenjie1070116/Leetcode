class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if not p:
            return False
        dp = [[False]*(len(p)+1) for _ in xrange(len(s)+1)]
        dp[0][0] = True
        for i in xrange(len(s)+1):
            if p[0] == '*':
                dp[i][1] = True
        for i in xrange(len(s)):
            for j in xrange(1, len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    for idx in xrange(i+1):
                        if dp[idx+1][j]:
                            dp[i+1][j+1] = True
                            break
        return dp[-1][-1]