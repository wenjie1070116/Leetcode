class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0]*(n+1)
    def lowbit(self, x):
        return x&(-x)
    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)
    def Sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res
       
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        snums = sorted(set(nums))
        hashmap = {}
        for i in xrange(len(snums)):
            hashmap[snums[i]] = i+1
        res = []
        FT = FenwickTree(len(snums))
        for i in xrange(len(nums)-1, -1, -1):
            res.append(FT.Sum(hashmap[nums[i]]-1))
            FT.add(hashmap[nums[i]],1)
        return res[::-1]
        