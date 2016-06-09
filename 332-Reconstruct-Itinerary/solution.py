class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets: return []
        hashmap = {}
        n = len(tickets)+1
        for ticket in tickets:
            if ticket[0] not in hashmap:
                hashmap[ticket[0]] = [ticket[1]]
            else:
                hashmap[ticket[0]].append(ticket[1])
        
        def dfs(hashmap, cur, res):
            if len(res) == n:
                return True
            if cur not in hashmap: return False
            places = sorted(hashmap[cur])
            for pla in places:
                res.append(pla)
                hashmap[cur].remove(pla)
                if dfs(hashmap, pla, res):
                    return res
                res.pop()
                hashmap[cur].append(pla)
        
        return dfs(hashmap, 'JFK', ['JFK'])
        
        
                
        