class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        snums = sorted(nums)
        for i in range(1, len(nums), 2)+range(0, len(nums), 2):
            nums[i] = snums.pop()