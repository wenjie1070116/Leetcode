class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        n = len(s)
        if n%2: return False
        stack = []
        for i in xrange(n):
            if not stack or s[i] in '([{':
                stack.append(s[i])
            else:
                if stack and 1<=ord(s[i])-ord(stack[-1])<=2:
                    stack.pop()
        return len(stack) == 0