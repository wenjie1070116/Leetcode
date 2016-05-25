class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A faster method
        if not nums: return
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)/2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid if nums[mid] != nums[end] else end-1
        return min(nums[start], nums[end])
        '''
        if not nums: return
        start, end = 0, len(nums)-1
        while start + 1 < end:
            while start + 1 < end and nums[start+1] == nums[start]:
                start += 1
            while start + 1 < end and nums[end-1] == nums[end]:
                end -= 1
            if start + 1 < end:
                mid = start + (end-start)/2
                if nums[mid] <= nums[start] or nums[end] >= nums[mid] >= nums[start]:
                    end = mid
                else:
                    start = mid
        return min(nums[start], nums[end])
        '''
        