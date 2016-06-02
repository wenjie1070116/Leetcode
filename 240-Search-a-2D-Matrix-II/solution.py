class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        start, end = -1, m
        while start + 1 < end:
            mid = start + (end-start)/2
            if matrix[mid][0] <= target:
                start = mid
            else:
                end = mid
        if matrix[start][-1] < target:
            return False
        s, e = -1, start+1
        while s + 1 < e:
            mid = s + (e-s)/2
            if matrix[mid][-1] < target:
                s = mid
            else:
                e = mid
        for i in xrange(e, start+1):
            l, r = -1, n
            while l + 1 < r:
                mid = l + (r-l)/2
                if matrix[i][mid] <= target:
                    l = mid
                else:
                    r = mid
            if matrix[i][l] == target:
                return True
        return False