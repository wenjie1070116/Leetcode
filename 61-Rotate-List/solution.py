# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        count = 0
        node = head
        tail = None
        while node:
            tail = node
            count += 1
            node = node.next
        k = k%count
        if k == 0: return head
        left = ListNode(0)
        right = ListNode(0)
        left.next = head
        node = head
        idx = 0
        while node:
            idx += 1
            if idx == count-k:
                right.next = node.next
                node.next = None
                break
            node = node.next
        tail.next = left.next
        left.next = None
        del left
        return right.next
        