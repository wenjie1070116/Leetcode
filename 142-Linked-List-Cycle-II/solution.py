# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = head
        mark = False
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                mark = True
                break
        if not mark: return None
        find = dummy
        while True:
            find = find.next
            slow = slow.next
            if find == slow:
                return slow