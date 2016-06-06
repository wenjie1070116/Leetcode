class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder: return False
        preorder = preorder.split(',')
        stack = []
        for i in xrange(len(preorder)):
            if not stack or preorder[i] != '#' or stack[-1] != '#':
                stack.append(preorder[i])
            else:
                while stack and stack[-1] == '#': # the while is very important since there maybe more than 1 '#' in the stack
                    stack.pop()
                    if not stack: return False
                    stack.pop()
                stack.append('#')
        return stack == ['#']
        