class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t: return True
        if len(s) != len(t): return False
        hashmap1 = {}
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
        