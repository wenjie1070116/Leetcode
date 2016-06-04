class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3: return
        nums.sort()
        res = sys.maxint
        for i in xrange(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start]+nums[end]+nums[i] == target:
                    return target
                elif nums[start]+nums[end]+nums[i] < target:
                    if abs(nums[start]+nums[end]+nums[i]-target) < abs(res-target):
                        res = nums[start]+nums[end]+nums[i]
                    start += 1
                else:
                    if abs(nums[start]+nums[end]+nums[i]-target) < abs(res-target):
                        res = nums[start]+nums[end]+nums[i]
                    end -= 1
        return res
        