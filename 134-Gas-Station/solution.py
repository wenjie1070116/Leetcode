class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost: return 0
        if len(gas) != len(cost): return -1
        diff = []
        for i in xrange(len(gas)):
            diff.append(gas[i]-cost[i])
        if sum(diff) < 0: return -1
        total = 0
        idx = -1
        for i in xrange(len(diff)):
            total += diff[i]
            if idx == -1:
                idx = i
            if total < 0:
                total = 0
                idx = -1
        return idx
        
        
        
        