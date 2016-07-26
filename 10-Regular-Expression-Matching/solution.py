class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False]*(len(p)+1) for _ in xrange(len(s)+1)]
        dp[0][0] = True
        for i in xrange(len(s)+1):
            for j in xrange(1, len(p)+1):
                if p[j-1] == '*':
                    a = dp[i][j-2] if j-2 >= 0 else False
                    b = dp[i][j-1]
                    c = dp[i-1][j] if (i-2 >= 0 and (p[i-2] == '.' or s[i-2] == p[j-2])) else False
                    dp[i][j] = a or b or c
                elif i == 0:
                    dp[i][j] = False
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                
        return dp[-1][-1]
        
        