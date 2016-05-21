import collections
class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        if not source or not target or len(source) < len(target): return ''
        if source == target: return source
        n = len(target)
        count = collections.Counter(target)
        total = 0
        res = source
        l, r, i = -1, -1, 0
        while i < len(source):
            if source[i] in count:
                if l == -1:
                    l = i
                count[source[i]] -= 1
                if count[source[i]] >= 0:
                    total += 1
                if total == n:
                    r = i
                    break
            i += 1
        if l == -1 or r == -1: return ''
        if r-l+1 == 1: return source[l:r+1]
        while l < r and (source[l] not in count or count[source[l]] < 0):
            if source[l] in count:
                count[source[l]] += 1
            l += 1
        if r-l+1 < len(res):
            res = source[l:r+1]
        while r < len(source):
            count[source[l]] += 1
            if count[source[l]] > 0:
                total -= 1
            l += 1
            while l < r and (source[l] not in count or count[source[l]] < 0):
                if source[l] in count:
                    count[source[l]] += 1
                l += 1
            while r < len(source) and total < n:
                r += 1
                if r < len(source) and source[r] in count:
                    count[source[r]] -= 1
                    if count[source[r]] >= 0:
                        total += 1
            if total == n and r-l+1 < len(res):
                res = source[l:r+1]
        return res