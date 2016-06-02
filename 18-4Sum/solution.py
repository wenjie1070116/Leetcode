class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4: return []
        nums.sort()
        res = []
        for i in xrange(len(nums)-3):
            if i != 0 and nums[i] == nums[i-1]: continue
            for j in xrange(i+1, len(nums)-2):
                if j != i+1 and nums[j] == nums[j-1]: continue
                goal = target - nums[i] - nums[j]
                start, end = j+1, len(nums)-1
                while start < end:
                    if nums[start]+nums[end] == goal:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        while start < end and nums[start] == nums[start-1]:
                            start += 1
                    elif nums[start]+nums[end] < goal:
                        start += 1
                    elif nums[start]+nums[end] > goal:
                        end -= 1
        return res
                    
                    
                    
        