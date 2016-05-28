class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) if s else 0
        if n < 2: return s
        s = list(s)
        start, end = 0, n-1
        while start < end:
            while start < end and s[start] not in 'aeiouAEIOU':
                start += 1
            while start < end and s[end] not in 'aeiouAEIOU':
                end -= 1
            if start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)
            