class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        hashmap = {'1':'*', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def dfs(pos, temp, res):
            if pos == len(digits):
                res.append(''.join([]+temp))
                return
            for ch in hashmap[digits[pos]]:
                temp.append(ch)
                dfs(pos+1, temp, res)
                temp.pop()
        res = []
        dfs(0, [], res)
        return res