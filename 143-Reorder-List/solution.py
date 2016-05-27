# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        prev = None
        while right:
            Next = right.next
            right.next = prev
            prev = right
            right = Next
        node = head
        while prev:
            prevNext = prev.next
            nodeNext = node.next
            node.next = prev
            prev.next = nodeNext
            prev = prevNext
            node = nodeNext
        return
        