class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) if nums else 0
        if n < 2: return False
        prenums = set()
        for i in xrange(n):
            if nums[i] in prenums:
                return True
            prenums.add(nums[i])
        return False