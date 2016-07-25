class Solution(object):
    
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
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
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
        dfs(0, temp, res)
        return res[0]