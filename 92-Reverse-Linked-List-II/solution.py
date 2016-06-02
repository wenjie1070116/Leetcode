# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        for i in xrange(m-1):
            node = node.next
        mid = node.next
        node.next = None
        mid_last = mid
        for i in xrange(m, n):
            mid_last = mid_last.next
        right = mid_last.next
        mid_last.next = None
        prev = None
        mid_head = mid
        while mid_head:
            Next = mid_head.next
            mid_head.next = prev
            prev = mid_head
            mid_head = Next
        node.next = prev
        mid.next = right
        return dummy.next
        