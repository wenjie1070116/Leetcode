class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s) if s else 0
        if n <= numRows or numRows == 1: return s # take care when numRows == 1
        res = ''
        for i in xrange(numRows):
            idx = i
            if idx == 0 or idx == numRows-1:
                while idx < n:
                    res += s[idx]
                    idx += 2*numRows-2
            else:
                while idx < n:
                    res += s[idx]
                    idx += 2*numRows-2-2*i
                    if idx < n:
                        res += s[idx]
                    idx += 2*i
        return res
        