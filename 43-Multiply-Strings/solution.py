class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2: return '0'
        res = [0]*(len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                val1 = ord(num1[i])-ord('0')
                val2 = ord(num2[j])-ord('0')
                res[i+j] += val1*val2
                if res[i+j] >= 10:
                    res[i+j+1] += res[i+j]/10
                    res[i+j] %= 10
        while res and res[-1] == 0: res.pop()
        res = [str(num) for num in res[::-1]]
        return ''.join(res) or '0'