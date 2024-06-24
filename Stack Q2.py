class LimitedStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
    
    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
        else:
            return self.stack.push()
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
