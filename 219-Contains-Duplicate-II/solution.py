class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        hashmap = {}
        for i in xrange(len(nums)):
            if nums[i] in hashmap and i-hashmap[nums[i]] <= k:
                return True
            hashmap[nums[i]] = i
        return False