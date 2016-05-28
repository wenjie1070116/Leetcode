# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node: return
        copy = UndirectedGraphNode(node.label)
        hashmap = {node.label:copy}
        traversed = set()
        stack = [node]
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.label in hashmap:
                    cur.neighbors.append(hashmap[neighbor.label])
                else:
                    hashmap[cur.label] = UndirectedGraphNode(neighbor.label)
                if neighbor.label not in traversed:
                    stack.append(neighbor)
            traversed.add(cur.label)
        return copy
                
        