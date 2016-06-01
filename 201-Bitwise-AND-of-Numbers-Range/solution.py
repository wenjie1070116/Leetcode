class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or m > n: return 0
        if m == n: return m
        temp = 1
        while temp < m:
            temp <<= 1
        if m < temp: 
            if n >= temp: return 0
            else:
                cur = self.rangeBitwiseAnd(m-temp/2, n-temp/2)
                return cur|(temp/2)
        elif m == temp:
            if n >= temp*2: return 0
            else:
                cur = self.rangeBitwiseAnd(m-temp, n-temp)
                return cur|temp
            
        
            