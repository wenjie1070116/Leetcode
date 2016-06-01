class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words) < 2: return 0
        res = 0
        bits = []
        idx = 0
        for word in words:
            temp = 0
            for ch in word:
                temp |= (1<<(ord(ch)-ord('a')))
            for i in xrange(len(bits)):
                if bits[i]&temp == 0:
                    res = max(res, len(words[i])*len(words[idx]))
            bits.append(temp)
            idx += 1
        return res
        