class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # a better way to write the code
        idx, total, res = 0, 1, 0
        while total <= n:
            if idx < len(nums) and nums[idx] <= total:
                total += nums[idx]
                idx += 1
            else:
                total <<= 1
                res += 1
        return res
        '''
        cur, total, res, i = 1, 0, 0, 0
        while i < len(nums) and total < n:
            if nums[i] > cur:
                while total < n and nums[i] > cur:
                    total += cur
                    cur = total+1
                    res += 1
            else:
                total += nums[i] # here total += nums[i] instead of cur since nums[i] <= cur
                cur = total+1
                i += 1
        while total < n:
            total += cur
            cur = total+1
            res += 1
        return res
        '''
        