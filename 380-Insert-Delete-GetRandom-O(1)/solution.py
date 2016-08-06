class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}
        self.Map = {}
        self.count = 0
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums: 
            return False
        self.nums[val] = self.count
        self.Map[self.count] = val
        self.count += 1
        return False
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.nums: return False
        idx = self.nums[val]
        self.nums.pop(val)
        self.count -= 1
        self.Map[idx] = self.Map[self.count]
        self.Map.pop(self.count)
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = randrange(0, self.count)
        return self.Map[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()