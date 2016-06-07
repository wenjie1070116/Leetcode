class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) if nums else 0
        if n < 3: return False
        
        stack = []
        for i in xrange(len(nums)):
            if not stack or nums[i] > stack[-1]:
                stack.append(nums[i])
                if len(stack) == 3: return True
            else:
                start, end = -1, len(stack)
                while start+1 < end:
                    mid = start+(end-start)/2
                    if stack[mid] < nums[i]:
                        start = mid
                    else:
                        end = mid
                stack[end] = nums[i]
        return False
        