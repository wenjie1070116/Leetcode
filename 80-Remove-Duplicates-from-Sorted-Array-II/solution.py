class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) if nums else 0
        if n < 2: return n
        target = nums[0]
        count = 0
        mark = True
        for i in xrange(1, n):
            if nums[i] == target and mark:
                nums[i-count] = nums[i]
                mark = False
            else:
                if nums[i] != target:
                    mark = True
                    target = nums[i]
                    nums[i-count] = nums[i]
                else:
                    count += 1
        return n-count
