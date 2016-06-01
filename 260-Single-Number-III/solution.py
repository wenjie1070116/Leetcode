class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) < 2: return
        total = 0
        for num in nums:
            total ^= num
        idx = 0
        while total&1 != 1:
            idx += 1
        num1, num2 = 0, 0
        mask = 1 << idx
        for num in nums:
            if num&mask:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
        