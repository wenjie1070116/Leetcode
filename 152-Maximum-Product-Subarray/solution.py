class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = Max = Min = nums[0]
        for i in xrange(1, len(nums)):
            temp = Max
            Max = max(Max*nums[i], Min*nums[i], nums[i])
            Min = min(Min*nums[i], temp*nums[i], nums[i])
            res = max(res, Max, Min)
        return res
        