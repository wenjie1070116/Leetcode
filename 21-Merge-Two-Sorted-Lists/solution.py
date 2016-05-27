# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        dummy = ListNode(0)
        node = dummy
        while l1 or l2:
            val1 = l1.val if l1 else sys.maxint
            val2 = l2.val if l2 else sys.maxint
            if val1 < val2:
                node.next = ListNode(val1)
                l1 = l1.next if l1 else None
            else:
                node.next = ListNode(val2)
                l2 = l2.next if l2 else None
            node = node.next
        return dummy.next