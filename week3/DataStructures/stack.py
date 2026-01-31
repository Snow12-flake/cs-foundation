class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
    
    def peek(self):
        return self.items[-1] if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(1); stack.push(2); stack.push(3)
    print(stack.pop())  # 3
    print(stack.peek()) # 2

