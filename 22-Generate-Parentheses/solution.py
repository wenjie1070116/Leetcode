class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 0: return []
        def dfs(left, right, temp, res):
            if left == right == n:
                res.append(''.join([]+temp))
                return
            if left >= right:
                if left == n:
                    temp.append(')')
                    dfs(left, right+1, temp, res)
                    temp.pop()
                else:
                    temp.append('(')
                    dfs(left+1, right, temp, res)
                    temp.pop()
                    
                    temp.append(')')
                    dfs(left, right+1, temp, res)
                    temp.pop()
        res = []
        dfs(0, 0, [], res)
        return res
        