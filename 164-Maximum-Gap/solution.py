class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2: return 0
        #bucket sort
        for i in xrange(32):
            buckets = [[],[]]
            mask = 1<<i
            for num in nums:
                if num&mask == 0:
                    buckets[0].append(num)
                else:
                    buckets[1].append(num)
            nums = buckets[0]+buckets[1]
        res = 0
        for i in xrange(1, len(nums)):
            if nums[i]-nums[i-1] > res:
                res = nums[i]-nums[i-1]
        return res
            
        
        