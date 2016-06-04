class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        nums.append('#')
        start = end = 0
        idx = 1
        res = []
        while idx < len(nums):
            if nums[idx] == nums[end]+1:
                end += 1
            else:
                if start == end:
                    res.append(str(nums[end]))
                else:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                start = end = idx
            idx += 1
                
        return res
            
        '''
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
        '''