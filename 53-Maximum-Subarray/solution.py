class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = -sys.maxint
        total = 0
        for i in xrange(len(nums)):
            total += nums[i]
            res = max(res, total)
            total = max(0, total)
        return res