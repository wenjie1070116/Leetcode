class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0 or not coins: return -1
        dp = [0]+[-1]*amount
        for i in xrange(amount):
            if dp[i] < 0:
                continue
            for c in coins:
                if i+c > amount:
                    continue
                if dp[i+c] < 0 or dp[i+c] > dp[i]+1:
                    dp[i+c] = dp[i]+1
        return dp[-1]