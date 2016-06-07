class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        snums = nums.sort()
        for i in range(0, len(nums), 2)+range(1, len(nums), 2):
            nums[i] = snums[i]
        