class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        hashmap = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        res = 0
        idx = 0
        while idx < len(s):
            if idx+1 < len(s) and s[idx:idx+2] in hashmap:
                res += hashmap[s[idx:idx+2]]
                idx += 2
            else:
                res += hashmap[s[idx]]
                idx += 1
        return res