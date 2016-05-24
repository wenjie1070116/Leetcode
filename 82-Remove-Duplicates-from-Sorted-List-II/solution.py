# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        prev = dummy
        while cur and cur.next:
            if cur.next.val == cur.val:
                while cur and cur.next and cur.next.val == cur.val:
                    cur = cur.next
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        prev.next = cur
        return dummy.next
                
        