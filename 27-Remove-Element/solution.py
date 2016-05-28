class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        count = 0
        for i in xrange(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                nums[i-count] = nums[i]
        return len(nums)-count