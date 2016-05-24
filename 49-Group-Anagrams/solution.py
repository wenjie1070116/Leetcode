class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs: return []
        res = []
        hashmap = {}
        for i in xrange(len(strs)):
            cur = ''.join(sorted(strs[i]))
            if cur in hashmap:
                hashmap[cur].append(strs[i])
            else:
                hashmap[cur] = [strs[i]]
        for key in sorted(hashmap.keys()):
            res.append(sorted(hashmap[key]))
        return res
            