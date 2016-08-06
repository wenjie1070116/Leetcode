class Solution(object):
    def select(self, nums, k):
        res = []
        if k == 0: return res
        n = len(nums)
        i = 0
        while i < n:
            if not res or len(res)+n-i==k:
                res.append(nums[i])
                i += 1
            elif nums[i] > res[-1]:
                res.pop()
            else:
                res.append(nums[i])
                i += 1
        return res[:k]
    # this part is very important
    def combine(self, nums1, nums2):
        res = []
        while nums1 or nums2:
            if nums1 > nums2:
                res += [nums1[0]]
                nums1 = nums1[1:]
            else:
                res += [nums2[0]]
                nums2 = nums2[1:]
        return res
    
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*k
        m, n = len(nums1), len(nums2)
        for i in xrange(min(k,m), max(0, k-n)-1, -1):
            sel1 = self.select(nums1, i)
            sel2 = self.select(nums2, k-i)
            cur = self.combine(sel1, sel2)
            res = max(res, cur)
        return res
        