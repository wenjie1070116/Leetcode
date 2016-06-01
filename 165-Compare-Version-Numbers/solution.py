class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        idx1, idx2 = 0, 0
        while idx1 < len(v1) or idx2 < len(v2):
            val1 = int(v1[idx1]) if idx1 < len(v1) else 0
            val2 = int(v2[idx2]) if idx2 < len(v2) else 0
            if val1 > val2: return 1
            elif val1 < val2: return -1
            else:
                idx1 += 1
                idx2 += 1
        return 0