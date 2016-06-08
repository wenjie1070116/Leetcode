class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(num, temp, cur, last, res):
            if not num:
                if cur == target:
                    res.append(temp)
                return
            for i in xrange(len(num)+1):
                now = num[:i]
                if i==1 or (i>1 and num[0] != '0'):
                    dfs(num[i:], temp+'+'+now, cur+int(now), int(now), res)
                    dfs(num[i:], temp+'-'+now, cur-int(now), -int(now), res)
                    dfs(num[i:], temp+'*'+now, cur-last+last*int(now), last*int(now), res)
        
        res = []
        for i in xrange(len(num)+1):
            if i == 1 or (i > 1 and num[0] != '0'):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res