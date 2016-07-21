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
                while Sum-nums[left] >= s:
                    Sum -= nums[left]
                    left += 1
                Min = min(Min, right-left+1)
            else:
                right += 1
        return Min
                
            
        