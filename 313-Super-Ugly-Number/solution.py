class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        hashmap = {prime:0 for prime in primes}
        while len(res) < n:
            Min = sys.maxint
            cur = None
            for prime in primes:
                if prime*res[hashmap[prime]] < Min:
                    Min = prime*res[hashmap[prime]]
                    cur = prime
                elif prime*res[hashmap[prime]] == Min:
                    hashmap[prime] += 1
            res.append(Min)
            hashmap[cur] += 1
        return res[-1]
        