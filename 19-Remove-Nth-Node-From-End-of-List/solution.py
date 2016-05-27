# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in xrange(n-1):
            fast = fast.next
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
        
        