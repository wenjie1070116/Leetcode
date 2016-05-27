# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        left = ListNode(0)
        l = left
        right = ListNode(0)
        r = right
        cur = head
        count = 1
        while cur:
            if count%2 == 1:
                l.next = cur
                l = l.next
            else:
                r.next = cur
                r = r.next
            cur = cur.next
            count += 1
        l.next = right.next
        return left.next
                
        