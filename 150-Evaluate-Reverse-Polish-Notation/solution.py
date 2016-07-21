class Solution(object):
    def div(self, a, b):
        sign = 1 if a*b >= 0 else -1
        a, b = abs(a), abs(b)
        return sign*(a/b)
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        hashmap = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/': self.div}
        res = []
        for i in xrange(len(tokens)):
            if tokens[i] in '+-*/':
                b = int(res.pop())
                a = int(res.pop())
                res.append(hashmap[tokens[i]](a,b))
            else:
                res.append(tokens[i])
        return int(res[0])
                
        