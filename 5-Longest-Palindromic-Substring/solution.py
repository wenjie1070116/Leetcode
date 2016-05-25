class Solution(object):
    def preprocess(self, s):
        new_s = list(s)
        new_s = '#'.join(new_s)
        return '#'+new_s+'#'
    
    def longestpalindrome(self, s):
        length = [0]*len(s)
        C, R = 0, 0
        for i in xrange(1, len(s)):
            if R < i: length[i] = 0
            else:
                mirror_i = 2*C-i
                length[i] = min(R-i, length[mirror_i])
            while i+1+length[i]<len(s) and i-1-length[i]>=0 and s[i+1+length[i]] == s[i-1-length[i]]:
                length[i] += 1
            if i+length[i] > R:
                C = i
                R = i+length[i]
        return length
            
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) if s else 0
        if n < 2: return s
        S = s
        s = self.preprocess(s)
        P = self.longestpalindrome(s)
        C, R = -1, -1
        for i in xrange(len(P)):
            if P[i] > R:
                C = i
                R = P[i]
        return S[(C-R)/2:(C-R)/2+R] 
      