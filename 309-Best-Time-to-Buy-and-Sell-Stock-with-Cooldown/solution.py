class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2: return 0
        buy = [0, -prices[0]]
        sell = [0, 0]
        for i in xrange(2, len(prices)+1):
            buy.append(max(sell[i-2]-prices[i-1], buy[i-1]+(prices[i-2]-prices[i-1])))
            sell.append(max(buy[i-1]+prices[i-1], sell[i-1]+(prices[i-1]-prices[i-2])))
        return max(sell)
        