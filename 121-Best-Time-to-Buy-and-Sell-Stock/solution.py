class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        Min = prices[0]
        res = 0
        for i in xrange(1, len(prices)):
            if prices[i] > Min:
                res = max(res, prices[i]-Min)
            else:
                Min = prices[i]
        return res