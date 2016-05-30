class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str: return True
        s = pattern
        t = str.split()
        if len(s) != len(t): return False
        hashmap1 = {} # two hashmap check, in case of this kind of example: 'aa', 'ab'
        hashmap2 = {}
        for i in xrange(len(s)):
            if t[i] in hashmap2:
                if s[i] != hashmap2[t[i]]:
                    return False
            else:
                hashmap2[t[i]] = s[i]
                
            if s[i] in hashmap1:
                if t[i] != hashmap1[s[i]]:
                    return False
            else:
                hashmap1[s[i]] = t[i]
        return True
        