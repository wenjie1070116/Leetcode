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
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        mid = self.findmid(head)
        root = TreeNode(mid.val)
        root.right = self.sortedListToBST(mid.next)
        mid.next = None
        root.left = self.sortedListToBST(head)
        return root
        