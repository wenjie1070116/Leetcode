class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        start, end = -1, len(nums)
        while start+1 < end:
            mid = start + (end-start)/2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        
        left, right = -1, len(nums)
        while left+1 < right:
            mid = left + (right-left)/2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if nums[start] == target:
            return [right, start]
        return [-1,-1]
        