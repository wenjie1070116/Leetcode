class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 
        res = [1]
        hashmap = {2:0, 3:0, 5:0}
        for i in xrange(1, n):
            cur = None
            if 3*res[hashmap[3]] >= 2*[hashmap[2]]:
                cur = 2
                if 3*res[hashmap[3]] == 2*[hashmap[2]]:
                    hashmap[3] += 1
            else:
                cur = 3
            
            if 5*res[hashmap[5]] < cur*res[hashmap[cur]]:
                cur = 5
            else:
                if cur*res[hashmap[cur]] == 5*[hashmap[5]]:
                    hashmap[5] += 1
            res.append(cur*res[hashmap[cur]])
            hahsmap[cur] += 1
        return res[-1]
                
                