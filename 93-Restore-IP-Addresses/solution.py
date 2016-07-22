class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) < 4:
            return []
        
        def dfs(pos, temp, res):
            if pos == len(s):
                if len(temp) == 4:
                    res.append('.'.join(temp))
                return
            if s[pos] == '0':
                temp.append(s[pos])
                dfs(pos+1, temp, res)
                temp.pop()
            else:
                for i in xrange(3):
                    if pos+i+1 <= len(s) and 0 <= int(s[pos:pos+i+1]) <= 255:
                        temp.append(s[pos:pos+i+1])
                        dfs(pos+i+1, temp, res)
                        temp.pop()
        res = []
        dfs(0, [], res)
        return res
                
        