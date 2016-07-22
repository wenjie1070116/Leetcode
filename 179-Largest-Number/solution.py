class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        if not nums: return '0'
        
        def comp(a, b):
            if int(str(a)+str(b)) > int(str(b)+str(a)):
                return -1
            else:
                return 1
        
        strs = [str(num) for num in nums]
        strs.sort(cmp=comp)
        
        if int(''.join(strs)) == 0: return '0'
        return ''.join(strs)