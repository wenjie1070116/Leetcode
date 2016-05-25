class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        m, n = len(words), len(words[0])
        
        def dfs(pos, wordhash):
            if not wordhash:
                return True
            cur = s[pos:pos+n]
            if cur in wordhash:
                wordhash[cur] -= 1
                if wordhash[cur] == 0:
                    wordhash.pop(cur)
                if dfs(pos+n, wordhash):
                    return True
            return False
        
        res = []
        for i in xrange(len(s)-m*n+1):
            wordhash = collections.Counter(words)
            if dfs(i, wordhash):
                res.append(i)
        return res
                
                