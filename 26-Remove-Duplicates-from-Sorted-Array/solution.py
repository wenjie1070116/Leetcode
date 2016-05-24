class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) if nums else 0
        if n < 2: return n
        target = nums[0]
        idx = 0
        for i in xrange(1, n):
            if nums[i] != target:
                target = nums[i]
                nums[i-idx] = nums[i]
            else:
                idx += 1
        return n-idx