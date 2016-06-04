# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        res = []
        for interval in intervals:
            if newInterval.end < interval.start:
                res.append(newInterval)
                newInterval = interval
            elif newInterval.start > interval.end:
                res.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        res.append(newInterval)
        return res