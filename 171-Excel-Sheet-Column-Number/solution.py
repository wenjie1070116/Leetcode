class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)):
            temp = ord(s[i])-ord('A')+1
            res = res*26+temp
        return res
        