# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        prev = None
        while fast:
            Next = fast.next
            fast.next = prev
            prev = fast
            fast = Next
        while prev and head:
            if prev.val != head.val: return False
            prev = prev.next
            head = head.next
        return True
            