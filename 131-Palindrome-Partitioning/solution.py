class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: return []
        
        def dfs(pos, temp, total, res):
            if pos == len(s):
                if total == len(s):
                    res.append([]+temp)
                return
            for i in xrange(pos, len(s)):
                for j in xrange(i+1, len(s)+1):
                    if s[i:j] == s[i:j][::-1]:
                        temp.append(s[i:j])
                        total += (j-i)
                        dfs(j, temp, total, res)
                        temp.pop()
                        total -= (j-i)
        
        res = []
        dfs(0, [], 0, res)
        return res