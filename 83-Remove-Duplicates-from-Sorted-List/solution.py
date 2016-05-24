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
        cur = head
        Next = head.next
        while Next:
            if Next.val == cur.val:
                Next = Next.next
            else:
                cur.next = Next
                cur = Next
                Next = Next.next
        cur.next = Next
        return head
        