class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        res = 0
        resarray = [nums[0]]
        # first -1 then 1
        mark = -1
        for i in xrange(1, len(nums)):
            if mark == -1:
                if nums[i] < resarray[-1]:
                    resarray.append(nums[i])
                    mark = 1
                else:
                    resarray[-1] = max(resarray[-1], nums[i])
            else:
                if nums[i] > resarray[-1]:
                    resarray.append(nums[i])
                    mark = -1
                else:
                    resarray[-1] = min(resarray[-1], nums[i])
        res = len(resarray)
        resarray = [nums[0]]
        # first 1 then -1
        mark = 1
        for i in xrange(1, len(nums)):
            if mark == -1:
                if nums[i] < resarray[-1]:
                    resarray.append(nums[i])
                    mark = 1
                else:
                    resarray[-1] = max(resarray[-1], nums[i])
            else:
                if nums[i] > resarray[-1]:
                    resarray.append(nums[i])
                    mark = -1
                else:
                    resarray[-1] = min(resarray[-1], nums[i])
        res = max(res, len(resarray))
        return res