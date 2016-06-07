class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes: return 0
        envelopes = sorted(envelopes, cmp = lambda x,y:x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        dp = []
        for i in xrange(len(envelopes)):
            if not dp or envelopes[i][1] > dp[-1][1]:
                dp.append(envelopes[i])
            else:
                start, end = -1, len(dp)
                while start + 1 < end:
                    mid = start + (end-start)/2
                    if dp[mid][1] >= envelopes[i][1]:
                        end = mid
                    else:
                        start = mid
                dp[end] = envelopes[i]
        return len(dp)