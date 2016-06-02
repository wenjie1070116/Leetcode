class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        s, e = -1, m
        while s + 1 < e:
            mid = s + (e-s)/2
            if matrix[mid][0] <= target:
                s = mid
            else:
                e = mid
        if matrix[s][-1] < target:
            return False
        start, end = -1, n
        while start + 1 < end:
            mid = start + (end-start)/2
            if matrix[s][mid] <= target:
                start = mid
            else:
                end = mid
        if matrix[s][start] == target:
            return True
        return False
        