class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        newnums = set()
        for num in nums:
            newnums.add(num)
        res = 0
        for num in nums:
            if num in newnums:
                temp = 1
                newnums.remove(num)
                left, right = num-1, num+1
                while left in newnums:
                    temp += 1
                    newnums.remove(left)
                    left -= 1
                while right in newnums:
                    temp += 1
                    newnums.remove(right)
                    right += 1
                res = max(res, temp)
        return res
            