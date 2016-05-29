class Solution(object):
    def firstbigger(self, nums, target):
        start, end = -1, len(nums)
        while start+1 < end:
            mid = start + (end-start)/2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        return end
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) if nums else 0
        if n < 2: return n
        stack = [nums[0]]
        for i in xrange(1, n):
            if nums[i] > stack[-1]:
                stack.append(nums[i])
            else:
                idx = self.firstbigger(stack, nums[i])
                stack[idx] = nums[i]
        return len(stack)
                
            
        