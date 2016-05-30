class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.popstack = []
        self.pushstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.pushstack:
            while self.popstack:
                self.pushstack.append(self.popstack.pop())
        self.pushstack.append(x)
            
    def pop(self):
        """
        :rtype: nothing
        """
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        self.popstack.pop()
        
    def peek(self):
        """
        :rtype: int
        """
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        return self.popstack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.popstack) == 0 and len(self.pushstack) == 0