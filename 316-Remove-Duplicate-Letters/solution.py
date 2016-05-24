import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) if s else 0
        if n < 2: return s
        count = collections.Counter(s)
        exist = set()
        res = []
        for i in xrange(n):
            if not res:
                res.append(s[i])
                exist.add(s[i])
            elif s[i] not in exist:
                while res and s[i] < res[-1] and count[res[-1]] != 0:
                    exist.remove(res[-1])
                    res.pop()
                res.append(s[i])
                exist.add(s[i])
            count[s[i]] -= 1
        return ''.join(res)