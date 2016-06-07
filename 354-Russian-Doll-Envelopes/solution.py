class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        envelopes = sorted(envelopes, key = lambda x:x[0])
        dp = [0]+[1]*len(envelopes)
        for i in xrange(len(envelopes)):
            for j in xrange(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i+1] = max(dp[i+1], dp[j+1]+1)
        return max(dp)