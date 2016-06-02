import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heaplist = []
        for i in xrange(k):
            heaplist.append(nums[i])
        heapq.heapify(heaplist)
        for i in xrange(k, len(nums)):
            heapq.heappush(heaplist, nums[i])
            heapq.heappop(heaplist)
        return heapq.heappop(heaplist)