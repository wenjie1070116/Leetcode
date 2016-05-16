import bisect
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        lines = []
        for building in buildings:
            lines.append([building[0], building[2]])
            lines.append([building[1], -building[2]])
        def comp(line1, line2):
            if line1[0] < line2[0]:
                return -1
            elif line1[0] > line2[0]:
                return 1
            else:
                if line1[1] > line2[1]:
                    return -1
                else:
                    return 1
        lines.sort(cmp=comp)
        heights = [0]
        res = []
        for line in lines:
            if line[1] > 0:
                if line[1] > heights[-1]:
                    res.append(line)
                bisect.insort(heights, line[1])
            else:
                heights.remove(abs(line[1]))
                if abs(line[1]) > heights[-1]:
                    res.append([line[0], heights[-1]])
        return res
                    
                    
                    