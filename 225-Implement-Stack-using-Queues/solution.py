class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.popqueue = collections.deque()
        self.pushqueue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.pushqueue:
            while self.popqueue:
                self.pushqueue.append(self.popqueue.pop())
        self.pushqueue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.popqueue:
            while self.pushqueue:
                self.popqueue.append(self.pushqueue.pop())
        self.popqueue.popleft()

    def top(self):
        """
        :rtype: int
        """
        if not self.popqueue:
            while self.pushqueue:
                self.popqueue.append(self.pushqueue.pop())
        return self.popqueue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.popqueue) == 0 and len(self.pushqueue) == 0
        