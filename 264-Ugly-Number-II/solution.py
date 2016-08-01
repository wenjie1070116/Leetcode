class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 
        res = [1]
        hashmap = {2:0, 3:0, 5:0}
        while len(res) != n:
            cur = 2
            if 3*res[hashmap[3]] < cur*res[hashmap[cur]]:
                cur = 3
            if 5*res[hashmap[5]] < cur*res[hashmap[cur]]:
                cur = 5
            if cur*res[hashmap[cur]] != res[-1]:
                res.append(cur*res[hashmap[cur]])
            hashmap[cur] += 1
        return res[-1]
                
                