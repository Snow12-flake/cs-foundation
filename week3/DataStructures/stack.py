class Stack:
    def __init__(self):
        # Initialize empty list to store stack items
        self.items = []
    
    def push(self, item):
        # ADD item to TOP of stack (end of list) -0(1)
        self.items.append(item)
    
    def pop(self):
        #REMOVE and RETURN top item - 0(1)
        if not self.is_empty():
            return self.items.pop()
        #Handle empty stack case
    
    def peek(self):
        # RETURN top item WITHOUT removing it -0(1)
        if not self.is_empty():
            return self.items[-1] # Last item in list
        return None # Empty stack

    def is_empty(self):
        # CHECK if stack has no items -0(1)
        return len(self.items) == 0

if __name__ == "__main__":
    s = Stack()
    print("Stack tests:")
    s.push("socks")
    s.push(2)
    s.push(3)
    s.push("shirt")

    print(s.pop())  # Should print 3
    print(s.peek()) # Should print 2
    print(s.is_empty())  # False
    while not s.is_empty():
        print(s.pop())  # 2, then 1
