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
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums: return 0
        Sum = [nums[0]]
        for i in xrange(1, len(nums)):
            Sum.append(Sum[-1]+nums[i])
        unique_Sum = sorted(set(Sum))
        hashmap = {}
        for i in xrange(len(unique_Sum)):
            hashmap[unique_Sum[i]] = i+1
        FT = FenwickTree(len(unique_Sum))
        res = 0
        for i in xrange(len(Sum)):
            left = bisect.bisect_left(unique_Sum, Sum[i]-upper)
            right = bisect.bisect_right(unique_Sum, Sum[i]-lower)
            res += FT.Sum(right) - FT.Sum(left) + (lower<=Sum[i]<=upper)
            FT.add(hashmap[Sum[i]], 1)
        return res
            
        