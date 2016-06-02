class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator*denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part = numerator/denominator
        numerator = numerator%denominator
        if numerator == 0:
            return sign+str(int_part)
        dec_part = ''
        hashmap = {}
        idx = 0
        while numerator != 0 and numerator not in hashmap:
            hashmap[numerator] = idx
            dec_part += str(numerator*10/denominator)
            numerator = numerator*10%denominator
            idx += 1
        if numerator in hashmap:
            pos = hashmap[numerator]
            dec_part = dec_part[:pos]+'('+dec_part[pos:]+')'
        return sign+str(int_part)+'.'+dec_part
        