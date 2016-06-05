import operator
import re
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.strip(' ')
        if not s: return 0
        def div(a, b):
            sign = 1 if a*b > 0 else -1
            return sign*(abs(a)/abs(b))
        hashmap = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':div}
        S = re.split('(\D)', s)
        s = []
        for ele in S:
            if ele != '' or ele != ' ':
                s.append(ele)
        nums = []
        ops = []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            if ch.isalnum() and ch != ' ':
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
        while ops:
            op = ops.pop()
            b = nums.pop()
            a = nums.pop()
            nums.append(hashmap[op](a,b))
        return nums[0]
                    