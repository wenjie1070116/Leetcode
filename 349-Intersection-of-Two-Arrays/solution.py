class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        res = []
        count = collections.Counter(nums1)
        for num in nums2:
            if num in count:
                res.append(num)
                count.pop(num)
        return res