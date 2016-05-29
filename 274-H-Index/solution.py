class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        count = collections.Counter(citations)
        cits = sorted(count.keys())
        idx = 0
        res = 0
        for i in xrange(len(cits)-1, -1, -1):
            idx += count[cits[i]]
            cur = min(idx, cits[i])
            res = max(res, cur)
        return res
            
        