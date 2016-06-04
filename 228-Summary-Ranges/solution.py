class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        idx = 0
        res = []
        temp = []
        while idx < len(nums):
            if not temp or nums[idx] == temp[-1]+1:
                temp.append(nums[idx])
                idx += 1
            else:
                if len(temp) == 1:
                    res.append(str(temp[0]))
                else:
                    res.append(str(temp[0])+'->'+str(temp[-1]))
                temp = []
        if len(temp) == 1:
            res.append(str(temp[0]))
        else:
            res.append(str(temp[0])+'->'+str(temp[-1]))
        return res