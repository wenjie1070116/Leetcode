class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return [1]
        for i in xrange(len(digits)-1, -1, 0):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        if digits[0] == 0:
            return [1]+digits
        return digits