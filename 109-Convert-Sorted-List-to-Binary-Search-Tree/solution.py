# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findmid(self, head):
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = fast = head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        dummy = ListNode(0)
        dummy.next = head
        prev = self.findmid(head)
        mid = prev.next
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        prev.next = None
        root.left = self.sortedListToBST(dummy.next)
        return root