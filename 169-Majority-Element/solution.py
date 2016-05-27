class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = None
        count = 0
        for i in xrange(len(nums)):
            if not res:
                res = nums[i]
                count = 1
            elif nums[i] != res:
                count -= 1
                if count == 0:
                    res = None
            else:
                count += 1
        return res