# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import collections
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points) if points else 0
        if n < 3: return n
        count = collections.Counter(points)
        unique_point = count.keys()
        res = 0
        for i in xrange(len(unique_point)):
            p1 = unique_point[i]
            hashmap = {}
            for j in xrange(i+1, len(unique_point)):
                p2 = unique_point[j]
                slop = None
                if p2.x-p1.x == 0:
                    slope = '#'
                else:
                    slope = (p2.y-p1.y)/(p2.x-p1.x)
                hashmap[slope] = hashmap.get(slope, 0)+1
            res = max(res,max(hashmap.values())+count[p1])
        return res
            
        
        