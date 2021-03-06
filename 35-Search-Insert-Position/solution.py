class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        start, end = -1, len(nums)
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        return end
        