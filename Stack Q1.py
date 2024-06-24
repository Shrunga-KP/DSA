class UnlimitedStack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
     if not self.is_empty():
       self.count-=1
       return self.data.pop()
     else:
        return None
    
    def peek(self):
        if self.is_empty():   
         return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)


# Example usage
# stack = UnlimitedStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print(stack.pop())  # Output: 3
# print(stack.peek())  # Output: 2
# print(stack.size())  # Output: 2
