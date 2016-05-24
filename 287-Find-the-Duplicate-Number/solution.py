class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return
        slow = fast = 0
        n = len(nums)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find
        