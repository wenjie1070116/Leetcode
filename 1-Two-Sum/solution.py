class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums) if nums else 0
        if n < 2: return []
        hashmap = {}
        for i in xrange(n):
            if target-nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i
        return []