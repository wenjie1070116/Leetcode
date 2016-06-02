# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k <= 1: return head
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        if k > count: return head
        dummy = ListNode(0)
        dummy.next = head
        group = count/k
        prev = dummy
        first = head
        node = head
        for i in xrange(group):
            before = None
            for j in xrange(k):
                Next = node.next
                node.next = before
                before = node
                node = Next
            prev.next = before
            first.next = node
            prev = first
            first = node
        return dummy.next
        
        