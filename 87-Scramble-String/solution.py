class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: return True
        if len(s1) != len(s2): return False
        n = len(s1)
        dp = [[[False]*n for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                dp[i][j][0] = s1[i]==s2[j]
        for k in xrange(1, n):
            for i in xrange(n-k-1, -1, -1):
                for j in xrange(n-k-1, -1, -1):
                    for m in xrange(k):
                        if (dp[i][j][m] and dp[i+m+1][j+m+1][k-m-1]) or (dp[i+k-m][j][m] and dp[i][j+m+1][k-m-1]):
                        #if (s1[i:i+m+1] == s2[j:j+m+1] and s1[i+m+1:i+k+1] == s2[j+m+1:j+k+1]) or (s1[i+k-m:i+k+1] == s2[j:j+m+1] and s1[i:i+k-m] == s2[j+m+1:j+k+1]):
                            dp[i][j][k] = True
                            break
        return dp[0][0][-1]
                    
                    
        
        
        """
        # Recursive method, TLE
        if s1 == s2: return True
        if len(s1) != len(s2): return False
        for i in xrange(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[len(s2)-i:len(s2)]) and self.isScramble(s1[i:], s2[:len(s2)-i])):
                return True
        return False
        """