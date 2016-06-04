# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        intervals.sort(cmp=comp)
        res = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if intervals[i].start > res[-1].end:
                res.append(intervals[i])
            else:
                #res[-1].start = min(res[-1].start, intervals[i].start)
                res[-1].end = max(res[-1].end, intervals[i].end)
        return res