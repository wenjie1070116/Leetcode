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
    def sortedListToBST(self, head):
        if not head: return None
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        def helper(length):
            if length <= 0: return None
            left = helper(length/2)
            root = TreeNode(self.node.val)
            self.node = self.node.next
            root.left = left
            root.right = helper(length-length/2-1)
            return root
        self.node = head
        return helper(count)
    
    '''
    def findmid(self, head):
        prev = None
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
        prev = self.findmid(head)
        if not prev:
            mid = head
            root = TreeNode(mid.val)
            root.right = self.sortedListToBST(mid.next)
            root.left = self.sortedListToBST(prev)
        else:
            mid = prev.next
            root = TreeNode(mid.val)
            root.right = self.sortedListToBST(mid.next)
            prev.next = None
            root.left = self.sortedListToBST(head)
        return root
        '''