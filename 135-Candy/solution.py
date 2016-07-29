class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        res = [1]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res.append(res[-1]+1)
            else:
                res.append(1)
        
        for i in xrange(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
        
        return sum(res)
        
        
        
            
        