class SegmentTreeNode(object):
    def __init__(self, start, end, Sum):
        self.start, self.end, self.Sum = start, end, Sum
        self.left = None
        self.right = None

class NumArray(object):
    
    def build(self, start, end, nums):
        if start > end: return None
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            root.Sum = nums[start]
        else:
            mid = start + (end-start)/2
            root.left = self.build(start, mid, nums)
            root.right = self.build(mid+1, end, nums)
            root.Sum = root.left.Sum + root.right.Sum
        return root
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = None
        if nums:
            self.root = self.build(0, len(nums)-1, nums)

    
    def updateTree(self, root, i, val):
        if not root or i < root.start or i > root.end: return
        if root.start == root.end == i:
            root.Sum = val
            return
        mid = root.start+(root.end-root.start)/2
        if i > mid:
            self.updateTree(root.right, i, val)
        else:
            self.updateTree(root.left, i, val)
        root.Sum = root.left.Sum+root.right.Sum
    
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        return self.updateTree(self.root, i, val)
        
    def sumTree(self, root, i, j):
        if not root or j < root.start or i > root.end: return 0
        if i <= root.start and j >= root.end:
            return root.Sum
        left = self.sumTree(root.left, i, j)
        right = self.sumTree(root.right, i, j)
        return left+right
    
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTree(self.root, i, j)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)