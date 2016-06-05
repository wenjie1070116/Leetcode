import operator
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        if not s: return 0
        def div(a, b):
            sign = 1 if a*b > 0 else -1
            return sign*(abs(a)/abs(b))
        hashmap = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':div}
        S = re.split('(\D)', s)
        s = []
        for ele in S:
            if ele != '' and ele != ' ':
                s.append(ele)
        nums = []
        ops = []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch.isalnum():
                nums.append(int(ch))
            elif ch in '+-*/':
                if ch in '*/':
                    a = nums.pop()
                    idx += 1
                    while s[idx] == ' ':
                        idx += 1
                    b = int(s[idx])
                    nums.append(hashmap[ch](a,b))
                else:
                    ops.append(ch)
            idx += 1
        for i in xrange(len(ops)):
            nums[0] = hashmap[ops[i]](nums[0], nums[i+1])
        return nums[0]
                    