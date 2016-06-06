class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height) if height else 0
        if n < 2: return 0
        Max = 0
        for i in xrange(1, n):
            if height[i] > height[Max]:
                Max = i
        left = 0
        res = 0
        for i in xrange(Max+1):
            if height[i] < height[left]:
                res += height[left]-height[i]
            else:
                left = i
                
        right = n-1
        for j in xrange(n-1, Max-1, -1):
            if height[j] < height[right]:
                res += height[right]-height[j]
            else:
                right = j
        return res