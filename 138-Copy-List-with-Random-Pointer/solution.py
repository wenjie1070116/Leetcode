# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        node = dummy
        copied = {}
        copy = None
        while head:
            if head not in copied:
                copied[head] = RandomListNode(head.label)
            copy = copied[head]
            if head.random:
                if head.random not in copied:
                    copied[head.random] = RandomListNode(head.random.label)
                copy.random = copied[head.random]
            node.next = copy
            node = node.next
            head = head.next
        return dummy.next
            
                