class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        n = len(x) if x else 0
        if n < 4: return False
        t1 = 0
        t2, t3, t4 = x[:3]
        increase = True if t4 > t2 else False
        for i in xrange(3, len(x)):
            t5 = x[i]
            if increase and t5<=t3:
                if t5+t1-t3<0 or (i+1<len(x) and x[i+1]+t2-t4<0):
                    increase = False
                elif i+1<len(x):
                    return True
            elif not increase and t5>=t3:
                return True
            t1, t2, t3, t4 = t2, t3, t4, t5
        return False
                
        