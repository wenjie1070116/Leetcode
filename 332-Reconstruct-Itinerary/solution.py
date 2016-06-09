class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets: return []
        hashmap = {}
        for ticket in tickets:
            if ticket[0] not in hashmap:
                hashmap[ticket[0]] = [ticket[1]]
            else:
                hashmap[ticket[0]].append(ticket[1])
        
        def dfs(hashmap, cur, temp, res):
            if not hashmap:
                res.append([]+temp)
                return res
            newhashmap = hashmap
            for pla in sorted(newhashmap[cur]):
                temp.append(pla)
                newhashmap[cur].remove(pla)
                if not newhashmap[cur]:
                    newhashmap.pop(cur)
                if dfs(newhashmap, pla, temp, res):
                    return res
                temp.pop()
                if cur not in newhashmap:
                    newhashmap[cur] = pla
                else:
                    newhashmap[cur].append(pla)
            return False
        
        return dfs(hashmap, 'JFK', ['JFK'], [])
        
        
                
        