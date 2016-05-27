class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count] = nums[i]
        for i in xrange(len(nums)-count, len(nums)):
            nums[i] = 0
        return
        