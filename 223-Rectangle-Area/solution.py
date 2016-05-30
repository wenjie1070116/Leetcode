class Solution(object):
    def Area(self, x1, x2, y1, y2):
        return abs(x1-x2)*abs(y1-y2)
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = self.Area(A, C, B, D)
        area2 = self.Area(E, G, F, H)
        intersect_area = 0
        if not (E >= C or G <= A or H <= B or F >= D):
            intersect_area = self.Area(max(A, E), min(C, G), min(H, D), max(F, B))
        return area1+area2-intersect_area
        
        