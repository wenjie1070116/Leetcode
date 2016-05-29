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
        traversed.add(node.label)
        stack = [node]
        while stack:
            cur = stack.pop()
            for neighbor in cur.neighbors:
                if neighbor.label not in traversed:
                    stack.append(neighbor)
                    traversed.add(neighbor.label)
                if neighbor.label not in hashmap:
                    hashmap[neighbor.label] = UndirectedGraphNode(neighbor.label)
                hashmap[cur.label].neighbors.append(hashmap[neighbor.label])
                
            
        return copy
                
        