class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        len_a, len_b = len(a)-1, len(b)-1
        carry = 0
        while len_a >= 0 or len_b >= 0:
            val_a = int(a[len_a]) if len_a >= 0 else 0
            val_b = int(b[len_b]) if len_b >= 0 else 0
            Sum = val_a+val_b+carry
            res.append(str(Sum%2))
            carry = Sum/2
            len_a -= 1
            len_b -= 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
            
        