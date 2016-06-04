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
        if not self.intervals or val > self.intervals[-1].end:
            if self.intervals and val == self.intervals[-1].end + 1:
                self.intervals[-1].end = val
            else:
                self.intervals.append(Interval(val, val))
        elif val < self.intervals[0].start:
            if val == self.intervals[0].start-1:
                self.intervals[0].start = val
            else:
                self.intervals = [Interval(val, val)]+self.intervals
        else:
            start, end = -1, len(self.intervals)
            while start+1 < end:
                mid = start+(end-start)/2
                if self.intervals[mid].start < val:
                    start = mid
                else:
                    end = mid
            idx = end
            if self.intervals[idx-1].end >= val or val == self.intervals[idx].start:
                return
            elif val-1 == self.intervals[idx-1].end and val+1 == self.intervals[idx].start:
                self.intervals[idx-1].end = self.intervals[idx].end
                self.intervals.remove(self.intervals[idx])
            elif val-1 == self.intervals[idx-1].end:
                self.intervals[idx-1].end = val
            elif val+1 == self.intervals[idx].start:
                self.intervals[idx].start = val
            else:
                self.intervals = self.intervals[:idx]+[Interval(val, val)]+self.intervals[idx:]

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()