class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or len(nums) < 2: return False
        hashmap = {}
        for i in xrange(len(nums)):
            for j in xrange(max(0, i-k), min(i+k, len(nums))+1):
                if j in hashmap and abs(nums[i]-hashmap[j])<=t:
                    return True
            hashmap[i] = nums[i]
        return False