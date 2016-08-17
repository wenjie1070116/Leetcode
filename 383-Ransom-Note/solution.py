import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote: return True
        if not magazine: return False
        count = collections.Counter(magazine)
        for ch in ransomNote:
            if ch not in count:
                return False
            else:
                count[ch] -= 1
                if count[ch] == 0:
                    count.pop(ch)
        return True