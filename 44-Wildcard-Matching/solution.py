class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p: return True
        if not p: return False
        s_i, p_i = 0, 0
        mark_p, mark_s = -1, -1
        while s_i < len(s):
            if p_i < len(p) and (s[s_i] == p[p_i] or p[p_i] == '?'):
                s_i += 1
                p_i += 1
            elif p_i < len(p) and p[p_i] == '*':
                mark_p = p_i
                mark_s = s_i
                p_i += 1
            elif mark_p != -1:
                p_i = mark_p + 1
                mark_s += 1
                s_i = mark_s
            else:
                return False
        while p_i < len(p) and p[p_i] == '*':
            p_i += 1
        return p_i == len(p) and s_i == len(s)