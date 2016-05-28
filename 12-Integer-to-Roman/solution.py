class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        signs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        for i in xrange(len(nums)):
            count = num/nums[i]
            res += signs[i]*count
            num %= nums[i]
        return res