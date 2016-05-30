class Solution(object):
    def findnth(self, nums1, l1, r1, nums2, l2, r2, n):
        if not nums1 and not nums2: return 
        len1 = r1-l1+1
        len2 = r2-l1+1
        if l1 > r1:
            return nums2[l2+n-1]
        if l2 > r2:
            return nums1[l1+n-1]
        if n == 1:
            return min(nums1[l1], nums2[l2])
        mid1 = nums1[(l1+r1+1)/2-1]
        mid2 = nums2[(l2+r2+1)/2-1]
        if mid1 < mid2:
            if n-(l1+r1+1)/2 == 0:
                return mid1
            return self.findnth(nums1, (l1+r1+1)/2, r1, nums2, l2, r2, n-(l1+r1+1)/2)
        else:
            if n-(l2+r2+1)/2 == 0:
                return mid2
            return self.findnth(nums1, l1, r1, nums2, (l2+r2+1)/2, r2, n-(l2+r2+1)/2)
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2: return 
        len1 = len(nums1) if nums1 else 0
        len2 = len(nums2) if nums2 else 0
        if (len1+len2)%2 == 1:
            return self.findnth(nums1, 0, len1-1, nums2, 0, len2-1, (len1+len2+1)/2)
        else:
            return (self.findnth(nums1, 0, len1-1, nums2, 0, len2-1, (len1+len2)/2)+self.findnth(nums1, 0, len1-1, nums2, 0, len2-1, (len1+len2)/2+1))/2.0