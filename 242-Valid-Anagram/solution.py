class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (not s and not t) or s == t: return True
        if len(s) != len(t): return False
        count = collections.Counter(s)
        for ch in t:
            if ch not in count: return False
            count[ch] -= 1
            if count[ch] == 0:
                count.pop(ch)
        return len(count) == 0