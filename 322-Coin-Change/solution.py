class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0 or not coins: return -1
        dp = [0]+[sys.maxint]*amount
        for coin in coins:
            for i in xrange(1, len(dp)):
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        res = dp[-1] if dp[-1] != sys.maxint else -1
        return res
        