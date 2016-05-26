class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        m, n = len(words), len(words[0])
        Words = collection.Counter(words)
        res = []
        resset = set()
        for i in xrange(len(s)-m*n+1):
            if i in resset:
                continue
            hashmap = {}
            count = 0
            left = i
            for j in xrange(i, len(s)-n+1, n):
                cur = s[j:j+n]
                if cur in Words:
                    hashmap[cur] = hashmap.get(cur, 0)+1
                    count += 1
                    while hashmap[cur] > Words[cur]:
                        hashmap[s[left:left+n]] -= 1
                        count -= 1
                        left += n
                    if count == m:
                        res.append(left)
                        resset.add(left)
                else:
                    left = j+n
                    count = 0
                    hashmap = {}
        return res
                    
            
        
        """
        # TLE
        if not s or not words: return []
        m, n = len(words), len(words[0])
        
        def dfs(pos, wordhash):
            if not wordhash:
                return True
            cur = s[pos:pos+n]
            if cur in wordhash:
                wordhash[cur] -= 1
                if wordhash[cur] == 0:
                    wordhash.pop(cur)
                if dfs(pos+n, wordhash):
                    return True
            return False
        
        res = []
        for i in xrange(len(s)-m*n+1):
            wordhash = collections.Counter(words)
            if dfs(i, wordhash):
                res.append(i)
        return res
        """
                
                