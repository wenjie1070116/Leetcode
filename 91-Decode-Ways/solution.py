class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [0]*(len(s)+1)
        if s[0] == '0': return 0
        dp[0] = 1
        dp[1] = 1
        for i in xrange(1, len(s)):
            if s[i] == '0':
                if s[i-1] not in '12':
                    return 0
                else:
                    dp[i+1] = dp[i-1]
            else:
                if s[i-1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                    dp[i+1] += dp[i-1]
                dp[i+1] += dp[i]
        return dp[-1]
                
            
                
            