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
        # in place
        if not head or not head.next: return head
        first = last = head.next
        prev = head
        cur = head.next.next
        while cur:
            last.next = cur.next
            prev.next = cur
            cur.next = first
            prev = cur
            last = last.next
            cur = last.next if last else None
        return head
        
        """
        if not head or not head.next: return head
        left = ListNode('a')
        l = left
        right = ListNode('b')
        r = right
        cur = head
        count = 1
        while cur:
            if count%2 == 1:
                l.next = ListNode(cur.val) #ListNode(cur.val) instead of cur
                l = l.next
            else:
                r.next = ListNode(cur.val)
                r = r.next
            cur = cur.next
            count += 1
        l.next = right.next
        return left.next
        """
                
        