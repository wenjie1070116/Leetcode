import operator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        def div(a, b):
            sign = 1 if a*b > 0 else -1
            return sign*(abs(a)/abs(b))
        hashmap = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':div}
        nums = []
        ops = []
        for ch in s:
            if ch == ' ':
                continue
            elif ch.isalnum():
                nums.append(int(ch))
            else:
                if ch in '*/':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(hashmap[ch](a,b))
                else:
                    ops.append(ch)
        while ops:
            op = ops.pop()
            b = nums.pop()
            a = nums.pop()
            nums.append(hashmap[op](a,b))
        return nums[0]
                    