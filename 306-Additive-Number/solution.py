class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num: return False
        def dfs(num, a, b):
            if not num:
                return True
            for i in xrange(1, len(num)+1):
                now = num[:i]
                if (i == 1 or (i>1 and num[0] != '0')) and int(now) == a+b and dfs(num[i:], b, int(now)):
                    return True
            return False
        for i in xrange(1, len(num)-1):
            if i == 1 or (i>1 and num[0] != '0'):
                for j in xrange(i+1,len(num)):
                    if j == i+1 or (j > i+1 and num[i] != '0'):
                        if dfs(num[j:], int(num[:i]), int(num[i:j])):
                            return True
        return False
        