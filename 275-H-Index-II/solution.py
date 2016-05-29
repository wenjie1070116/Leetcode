class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        start, end = 0, len(citations)-1
        while start + 1 < end:
            mid = start + (end-start)/2
            if len(citations)-mid >= citations[mid]:
                start = mid
            else:
                end = mid
        return max(min(citations[start],len(citations)-start), min(citations[end],len(citations)-end))
        
        