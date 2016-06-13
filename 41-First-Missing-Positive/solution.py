class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        numset = set(nums)
        n = len(nums)
        for i in xrange(1, n+2):
            if i not in numset:
                return i
        
        
        '''
        if not nums:
            return 1
        for i in xrange(len(nums)):
            while nums[i] > 0 and nums[i] != i+1 and nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1]:
                # can not write as 'nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]', cause nums[nums[i]-1] depends on 
                # nums[i] but this sentence nums[i] has changed at the very beginning, be careful about that
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        '''
        