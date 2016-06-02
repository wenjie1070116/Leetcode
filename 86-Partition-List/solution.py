# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next and node.next.val < x:
                node = node.next
        Next = node.next
        while Next and Next.next:
            if Next.next.val >= x:
                Next = Next.next
            else:
                temp = Next.next
                Next.next = temp.next
                temp.next = node.next
                node.next = temp
                node = node.next
        return dummy.next
