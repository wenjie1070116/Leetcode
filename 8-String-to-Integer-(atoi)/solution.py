class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0
        value = 0
        sign = 1
        if str[0] == '-':
            sign = -1
        elif str[0] in '0987654321':
            value = int(str[0])
        elif str[0] != '+':
            return sign*value
        
        for i in xrange(1, len(str)):
            if str[i] in '0987654321':
                value = value*10+int(str[i])
            else:
                break
        
        if sign*value > 2**31-1: return 2**31-1
        if sign*value < -2**31: return -2**31
        return sign*value