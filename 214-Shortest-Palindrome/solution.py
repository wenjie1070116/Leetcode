class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[: len(s) - p[-1]] + s
        
        """
        n = len(s) if s else 0
        if n <= 1: return s
        rev_s = s[::-1]
        for i in xrange(n, 0, -1):
            if s[:i] == rev_s[n-i:]:
                return rev_s[:n-i]+s
        """
        