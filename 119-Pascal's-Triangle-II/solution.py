class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0: return []
        if rowIndex == 0: return [1]
        row = [1,1]
        for i in xrange(2, rowIndex+1):
            cur = []
            for j in xrange(i+1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(row[j-1]+row[j])
            row = cur
        return row
        