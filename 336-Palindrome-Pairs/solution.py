class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if not words or len(words) < 2: return []
        hashmap = {}
        res = []
        for i in xrange(len(words)):
            hashmap[words[i]] = i
        for j in xrange(len(words)):
            word = words[j]
            # take care of the details, when '' exists or when another word == word[::-1]
            for k in xrange(len(word)+1): # k's range
                # remember to check whether remaining part is palindrome itself
                if word[:k][::-1] in hashmap and hashmap[word[:k][::-1]] != j and word[k:]==word[k:][::-1]:
                    res.append([j, hashmap[word[:k][::-1]]])
            for m in xrange(1,len(word)+1): # m's range
                if word[m:][::-1] in hashmap and hashmap[word[m:][::-1]] != j and word[:m]==word[:m][::-1]:
                    res.append([hashmap[word[m:][::-1]], j])
        return res