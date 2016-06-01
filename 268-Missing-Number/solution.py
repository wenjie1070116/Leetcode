class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        total = (n+1)*n/2
        for num in nums:
            total -= num
        return total