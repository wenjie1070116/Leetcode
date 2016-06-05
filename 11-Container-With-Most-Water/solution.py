class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) if height else 0
        if n < 2: return 0
        start, end = 0, n-1
        res = 0
        while start < end:
            res = max(res, min(height[start], height[end])*(end-start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res
        