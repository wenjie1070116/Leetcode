class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        idx = len(nums)-1
        while idx >= 0:
            if idx > 0 and nums[idx-1] < nums[idx]:
                idx -= 1
                break
            idx -= 1
        if idx == -1:
            nums[:] = nums[::-1]
            return
        i = len(nums)-1
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[idx]:
                break
        nums[idx], nums[i] = nums[i], nums[idx]
        nums[idx+1:] = nums[idx+1:][::-1]