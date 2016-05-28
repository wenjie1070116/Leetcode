# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        prev = head
        cur = head.next
        while cur:
            if cur.val > prev.val:
                prev = cur
                cur = cur.next
            else:
                node = dummy
                while node.next.val < cur.val:
                    node = node.next
                Next = node.next
                node.next = cur
                prev.next = cur.next
                cur.next = Next
                cur = prev.next
        return dummy.next