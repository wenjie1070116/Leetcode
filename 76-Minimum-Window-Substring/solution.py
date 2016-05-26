class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t): return ''
        counter = collections.Counter(t)
        hashmap = {}
        count = 0
        start = 0
        res = s+'#'
        for i in xrange(len(s)):
            if s[i] in counter:
                hashmap[s[i]] = hashmap.get(s[i], 0)+1
                if hashmap[s[i]] <= counter[s[i]]:
                    count +=1
                while s[start] not in counter or hashmap[s[start]] > counter[s[start]]:
                    if s[start] in hashmap:
                        hashmap[s[start]] -= 1
                    start += 1
                if count == len(t) and i-start+1 < len(res):
                    res = s[start:i+1]
        if res == s+'#': return ''
        return res