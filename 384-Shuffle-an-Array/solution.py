class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        self.Nums = nums
        self.count = len(nums)
        self.n = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.n = self.count
        self.Nums = self.nums
        return self.Nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = []
        idx = randrange(0, self.n)
        res.append(self.Nums[idx])
        self.n -= 1
        self.Nums[idx] = self.Nums[self.n]
        self.Nums.pop()
        while self.Nums:
            idx = randrange(0, self.n)
            res.append(self.Nums[idx])
            self.n -= 1
            self.Nums[idx] = self.Nums[self.n]
            self.Nums.pop()
        self.Nums = res
        self.n = self.count
        return self.Nums
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()