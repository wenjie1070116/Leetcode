# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points) if points else 0
        if n < 3: return n
        count = {}
        for point in points:
            count[(point.x, point.y)] = count.get((point.x, point.y), 0)+1
        unique_point = count.keys()
        if len(unique_point) == 1: return count[unique_point[0]] #be careful when all the points is the same
        res = 0
        for i in xrange(len(unique_point)-1):
            p1 = unique_point[i]
            hashmap = {}
            for j in xrange(i+1, len(unique_point)):
                p2 = unique_point[j]
                slop = None
                if p2[0]-p1[0] == 0:
                    slope = '#'
                else:
                    slope = float(p2[1]-p1[1])/(p2[0]-p1[0])# take care the divide result should be float
                hashmap[slope] = hashmap.get(slope, 0)+count[p2] #take care that p2 may have duplicate points
            res = max(res,max(hashmap.values())+count[p1])
        return res