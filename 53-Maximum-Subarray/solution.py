class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = -sys.maxint # initial value of res should be set to -sys.maxint since num in nums might < 0
        total = 0
        for i in xrange(len(nums)):
            total += nums[i]
            res = max(res, total)
            total = max(0, total)
        return res