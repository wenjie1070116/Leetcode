class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        Sum, left, right, i, Min = 0, 0, 0, 0, sys.maxint
        while right < len(nums):
            Sum += nums[right]
            if Sum >= s:
                while left < right and Sum-nums[left] >= s:
                    Sum -= nums[left]
                    left += 1
                Min = min(Min, right-left+1)
                if Min == 1 or right == len(nums)-1: return Min
                Sum -= nums[left]
                left += 1
                right += 1
            else:
                right += 1
        return 0 if Min == sys.maxint else Min
                
            
        