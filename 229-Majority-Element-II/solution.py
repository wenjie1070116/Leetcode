class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            elif len(hashmap) < 2:
                hashmap[num] = 1
            else:
                for key in hashmap.keys():
                    hashmap[key] -= 1
                    if hashmap[key] == 0:
                        hashmap.pop(key)
        keys = hashmap.keys()
        hashmap = {key:0 for key in keys}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
        res = []
        for key in keys:
            if hashmap[key] > len(nums)/3:
                res.append(key)
        return res