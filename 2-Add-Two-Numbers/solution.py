# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        h1 = l1
        h2 = l2
        res = ListNode(0)
        cur = res
        carry = 0
        while h1 or h2:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0
            Sum = val1+val2+carry
            cur.next = ListNode(Sum%10)
            cur = cur.next
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            carry = Sum/10
        if carry:
            cur.next = ListNode(carry)
        return res.next
            
            
            
            
            