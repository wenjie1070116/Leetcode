class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        for i in xrange(len(nums)-1):
            left.append(nums[i]*left[-1])
        temp = 1
        for i in xrange(len(nums)-1, 0, -1):
            temp *= nums[i]
            left[i-len(nums)-1] *= temp
        return left