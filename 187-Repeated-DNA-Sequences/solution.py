class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 11:
            return []
        hashmap = {}
        res = []
        for i in xrange(len(s)-9):
            hashmap[s[i:i+10]] = hashmap.get(s[i:i+10], 0)+1
            if hashmap[s[i:i+10]] == 2:
                res.append(s[i:i+10])
        return res