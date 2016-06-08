class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = max(0, -dungeon[-1][-1])+1
        for i in xrange(m-2, -1, -1):
            dungeon[i][n-1] = max(1, dungeon[i+1][n-1]-dungeon[i][n-1])
        for j in xrange(n-2, -1, -1):
            dungeon[m-1][j] = max(1, dungeon[m-1][j+1]-dungeon[m-1][j])
        for i in xrange(m-2, -1, -1):
            for j in xrange(n-2, -1, -1):
                dungeon[i][j] = max(1, min(dungeon[i+1][j], dungeon[i][j+1])-dungeon[i][j])
        return dungeon[0][0]