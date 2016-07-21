class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) if s else 0
        if n <= 1: return s
        rev_s = s[::-1]
        for i in xrange(n, 0, -1):
            if s[:i] == rev_s[n-i:]:
                return rev_s[:n-i]+s
        