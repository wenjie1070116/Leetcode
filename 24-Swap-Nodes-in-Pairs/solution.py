# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = head
        last = head.next
        while first and last:
            prev.next = last
            first.next = last.next
            last.next = first
            prev = first
            first = first.next
            last = first.next if first else None
        return dummy.next