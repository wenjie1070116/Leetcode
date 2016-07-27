class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def maxsubarraylessk(arr, k):
            cumset = []
            cumset.append(0)
            maxsum = -sys.maxint
            cursum = 0
            for num i arr:
                cursum += num
                idx = bisect.bisect_left(cumset, cursum-k)
                if 0<=idx<len(cursum):
                    maxsum = max(maxsum, cursum-cumset[idx])
                bisect.insort(cumset, cursum)
            return maxsum
        
        if not matrix: return 0
        row, col = len(matrix), len(matrix[0])
        res = -sys.maxint
        for left in xrange(col):
            cursum = [0]*row
            right = left
            while right < col:
                for i in xrange(row):
                    cursum[i] += matrix[i][right]
                curarrmax = maxsubarraylessk(cursum, k)
                res = max(res, curarrmax)
                right += 1
        return res
        