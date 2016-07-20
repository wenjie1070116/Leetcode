class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0: return [0]
        res = [0, 1]
        for i in xrange(2, n+1):
            temp = res[:]
            for num in res[::-1]:
                temp.append(num+2**(i-1))
                
            res = temp[:]
        return res