class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 : return False
        if num == 1: return True
        start, end = 0, 16
        while start+1 < end:
            mid = start + (end-start)/2
            if num == (2**mid)**2:
                return True
            elif num < (2**mid)**2:
                end = mid
            else:
                start = mid
        l, r = 2**start, 2**end
        while l+1 < r:
            m = l + (r-l)/2
            if num == m**2:
                return True
            elif num < m**2:
                r = m
            else:
                l = m
        return False
            