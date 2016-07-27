class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = []
        res = 0
        for i in xrange(len(s)):
            if stack and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
       stack.append(len(s))
       for i in xrange(1, len(stack)):
           res = max(res, stack[i]-stack[i-1]-1)
       return res