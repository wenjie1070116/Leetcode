class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs[0]) == 0: return '' # take care that strs[0] may be '' empty
        i = 0
        while True:
            if i == len(strs[0]):
                return strs[0][:i] # check whether i out of strs[0] index
            target = strs[0][i]
            for j in xrange(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != target:
                    return strs[0][:i]
            i += 1
        
                
        