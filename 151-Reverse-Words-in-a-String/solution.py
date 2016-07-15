class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if not s: return s
        words = s.split(' ')
        onlywords = []
        for i in xrange(len(words)):
            if words[i] != '' and words[i] != ' ':
                onlywords.append(words[i][::-1])
        res = ' '.join(onlywords)
        return res[::-1]