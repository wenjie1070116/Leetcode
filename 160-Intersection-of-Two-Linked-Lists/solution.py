# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = headA
        node = dummy
        while node.next:
            node = node.next
        node.next = headB
        slow = dummy
        fast = dummy
        mark = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                mark = True
                break
        if not mark: 
            del dummy
            node.next = None
            return None
        find = dummy
        while True:
            find = find.next
            slow = slow.next
            if find == slow:
                del dummy
                node.next = None
                return slow
        