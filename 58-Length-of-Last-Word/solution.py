class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        mark = False
        for i in xrange(len(s)-1, -1, -1):
            if s[i] == ' ':
                if not mark:
                    continue
                else:
                    return res
            else:
                if not mark:
                    mark = True
                res += 1
        return res
                