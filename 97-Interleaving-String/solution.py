class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        if len(s3) != len(s1)+len(s2):
            return False
        dp = [[False]*(len(s2)+1) for _ in xrange(len(s1)+1)]
        dp[0][0] = True
        
        for i in xrange(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        
        for j in xrange(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]
        
        for i in xrange(1, len(s1)+1):
            for j in xrange(1, len(s2)+1):
                a, b = False, False
                if s1[i-1] == s3[i+j-1]:
                    a = dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:
                    b = dp[i][j-1]
                dp[i][j] = a or b
        
        return dp[-1][-1]
            
        