class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 1: return []
        if not edges: return [i for i in xrange(n)]
        neighbors = [[] for i in xrange(n)]
        indegree = [0]*n
        for edge in edges:
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        res = {i for i in xrange(n)}
        while len(res) > 2:
            temp = []
            for i in res:
                if indegree[i] == 1:
                    temp.append(i)
            for idx in temp:
                for neighbor in neighbors[idx]:
                    indegree[neighbor] -= 1
                res.remove(idx)
        res = list(res)
        return res
            
            
        