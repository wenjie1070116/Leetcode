class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        N = m+n-1
        n1 = m-1
        n2 = n-1
        while n1 >= 0 or n2 >= 0:
            val1 = nums1[n1] if n1 >= 0 else -sys.maxint
            val2 = nums2[n2] if n2 >= 0 else -sys.maxint
            if val1 > val2:
                nums1[N] = val1
                n1 -= 1
            else:
                nums1[N] = val2
                n2 -= 1
            N -= 1