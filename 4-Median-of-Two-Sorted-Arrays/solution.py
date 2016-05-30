class Solution(object):
    def findnth(self, nums1, nums2, n):
        if not nums1 and not nums2: return 
        len1 = len(nums1) if nums1 else 0
        len2 = len(nums2) if nums2 else 0
        if len1 == 0:
            return nums2[n-1]
        if len2 == 0:
            return nums1[n-1]
        if n == 1:
            return min(nums1[0], nums2[0])
        mid1 = nums1[(len1+1)/2-1]
        mid2 = nums2[(len2+1)/2-1]
        if mid1 < mid2:
            return self.findnth(nums1[(len1+1)/2:], nums2, n-(len1+1)/2)
        else:
            return self.findnth(nums1, nums2[(len2+1)/2:], n-(len2+1)/2)
        
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
            return self.findnth(nums1, nums2, (len1+len2)/2)
        else:
            return (self.findnth(nums1, nums2, (len1+len2)/2)+self.findnth(nums1, nums2, (len1+len2)/2+1))/2.0