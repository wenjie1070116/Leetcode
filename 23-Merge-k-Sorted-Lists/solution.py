# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dummy = ListNode(0)
        cur = dummy
        heaplist = []
        for list in lists:
            if list:
                heaplist.append((list.val, list))
        heapq.heapify(heaplist)
        while heaplist:
            node = heapq.heappop(heaplist)
            cur.next = node[1]
            cur = cur.next
            if node[1].next:
                heapq.heappush(heaplist, (node[1].next.val, node[1].next))
        return dummy.next
        
        