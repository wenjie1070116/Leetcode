class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2 or word1 == word2: return 0
        if not word1: return len(word2)
        if not word2: return len(word1)
        dp = [[0]*(len(word2)+1) for _ in xrange(len(word1)+1)]
        for i in xrange(1, len(word1)+1):
            dp[i][0] = i
        for j in xrange(1, len(word2)+1):
            dp[0][j] = j
        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        return dp[-1][-1]
        