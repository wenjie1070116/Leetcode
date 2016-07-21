class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s: return True
        if not wordDict: return False
        
        def dfs(pos):
            if pos >= len(s):
                return True
            for i in xrange(1, len(s)-pos+1):
                if s[pos:pos+i] in wordDict and dfs(pos+i):
                    return True
            return False
        
        
        return dfs(0)