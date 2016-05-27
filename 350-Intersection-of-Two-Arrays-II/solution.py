class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        count = collections.Counter(nums1)
        res = []
        for i in xrange(len(nums2)):
            if nums2[i] in count:
                res.append(nums2[i])
                count[nums2[i]] -= 1
                if count[nums2[i]] == 0:
                    count.pop(nums2[i])
        return res