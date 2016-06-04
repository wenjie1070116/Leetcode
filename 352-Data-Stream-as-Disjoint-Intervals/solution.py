# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        s = self.intervals
        if not s or val > s[-1].end:
            if val == s[-1].end + 1:
                s[-1].end = val
            else:
                s.append(Interval(val, val)
        elif val < s[0].start:
            if val == s[0].start-1:
                s[0].start = val
            else:
                s = [Interval(val, val)]+s
        else:
            idx = bisect.bisect_left(Interval(val, val))
            if s[idx-1].end == val or val == s[idx].start:
                return
            elif s[idx-1].end+1 == val == s[idx].start-1:
                s[idx-1].end = s[idx].end
                s.remove(s[idx])
            elif s[idx-1].end+1 == val:
                s[idx-1].end == val
            elif s[idx].start-1 == val:
                s[idx].start = val
            else:
                s = s[:idx]+[Interval(val, val)]+s[idx:]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()