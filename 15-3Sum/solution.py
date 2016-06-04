class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3: return []
        nums.sort()
        res = []
        for i in xrange(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start]+nums[end] == -nums[i]:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums[start]+nums[end] < -nums[i]:
                    start += 1
                else:
                    end -= 1
        return res