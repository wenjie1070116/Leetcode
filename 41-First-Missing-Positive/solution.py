class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] != i+1 and nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1] 
                nums[nums[i]-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
        