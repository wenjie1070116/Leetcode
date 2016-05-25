class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        start, end = 0, len(nums)-1
        while start + 1 < end:
            while start + 1 < end and nums[start+1] == nums[start]:
                start += 1
            while start + 1 < end and nums[end-1] == nums[end]:
                end -= 1
            if start + 1 < end:
                mid = start + (end-start)/2
                if nums[mid] >=target>=nums[start] or (nums[mid] < nums[start] and (target >= nums[start] or target <= nums[mid])):
                    end = mid
                else:
                    start = mid
        if nums[start] == target or nums[end] == target: return True
        return False