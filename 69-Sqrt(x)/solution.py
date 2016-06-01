class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0: return
        start, end = -1, x+1
        while start + 1 < end:
            mid = start + (end-start)/2
            if mid*mid <= x:
                start = mid
            else:
                end = mid
        return start