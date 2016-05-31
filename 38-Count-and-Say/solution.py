class Solution(object):
    def say(self, num):
        res = 0
        digit = None
        count = 0
        while num:
            digit = num%10
            count = 1
            num /= 10
            while num%10 == digit:
                count += 1
                num /= 10
            res = res*10+digit
            res = res*10+count
        result = 0
        while res:
            result = result*10+res%10
            res /= 10
        return result
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return
        if n == 1:
            return '1'
        return str(self.say(int(self.countAndSay(n-1))))
        