class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        i = 0
        while True:
            target = strs[0][i]
            for j in xrange(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != target:
                    return strs[0][:i]
            i += 1
        
                
        