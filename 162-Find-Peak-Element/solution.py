class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = -1, len(nums)
        while start+1 < end:
            mid = start + (end-start)/2
            if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid
        num_s = nums[start] if start != -1 else -sys.maxint
        num_e = nums[end] if end != len(nums) else -sys.maxint
        if num_e > num_s: return end
        else: return start
        