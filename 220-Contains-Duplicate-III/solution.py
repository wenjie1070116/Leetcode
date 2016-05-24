class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or len(nums) < 2 or k < 1 or t < 0: return False
        hashmap = {}
        for i in xrange(len(nums)):
            cur = nums[i]/t if t > 0 else nums[i]
            for j in (cur-1, cur, cur+1):
                if j in hashmap and i-hashmap[j] <= k and abs(nums[hashmap[j]]-nums[i]) <= t:
                    return True
            hashmap[cur] = i
        return False
        