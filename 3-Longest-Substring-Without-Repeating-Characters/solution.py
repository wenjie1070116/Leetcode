class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) if s else 0
        if n < 2:
            return n
        prev = hashmap{s[0]:0}
        res = 1
        start = 0
        for i in xrange(1, len(s)):
            if s[i] in prev:
                start = hashmap[s[i]]+1
            res = max(res, i-start+1)
            hashmap[s[i]] = i
        return res