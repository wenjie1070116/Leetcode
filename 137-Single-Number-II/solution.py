class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            temp = 0
            for j in xrange(len(nums)):
                temp += nums[j]&1
                nums[j] >>= 1
            res |= (temp%3)<<i
        if res <= 2**31-1:
            return res
        return -2**32+res
        