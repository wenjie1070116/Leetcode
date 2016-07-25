class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]*(target+1)
        dp[0] = 1
        for i in xrange(target+1):
            for num in nums:
                dp[x+num] += dp[x]
        return dp[-1]
    
    """ TLE
    def factor(self, n):
        res = 1
        for i in xrange(1, n+1):
            res *= i
        return res
        
    def situations(self, nums):
        n = len(nums)
        res = self.factor(n)
        count = collections.Counter(nums)
        for num in count:
            res /= self.factor(count[num])
        return res
        
    def combinationSum4(self, nums, target):
        """
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        if not nums: return 0
        nums.sort()
        def dfs(pos, temp, res):
            if sum(temp) == target:
                res[0] += self.situations(temp)
                return
            if sum(temp) > target:
                return
            for i in xrange(pos, len(nums)):
                temp.append(nums[i])
                dfs(i, temp, res)
                temp.pop()
        res = [0]
        dfs(0, [], res)
        return res[0]
    """