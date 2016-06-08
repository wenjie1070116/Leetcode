import operator
import re
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if not str: return []
        hashmap = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        inp = re.split('(\D)', input)
        nums = []
        ops = []
        for ele in inp:
            if ele.isalnum():
                nums.append(int(ele))
            else:
                ops.append(ele)
        
        def cal(nums, ops):
            if not ops: return [nums[0]]
            res = []
            for i in xrange(len(ops)):
                left = cal(nums[:i+1], ops[:i])
                right = cal(nums[i+1:], ops[i+1:])
                for l in left:
                    for r in right:
                        res.append(hashmap[ops[i]](l, r))
            return res
        
        return cal(nums, ops)
        
        