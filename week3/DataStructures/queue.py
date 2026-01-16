from collections import deque  # Efficient for left pops

class Queue:
    def __init__(self):
        # Use deque for O(1) operations on both ends
        self.items = deque()
    
    def enqueue(self, item):
        # ADD to REAR (right end) - FIFO - O(1)
        self.items.append(item)
    
    def dequeue(self):
        # REMOVE from FRONT (left end) - O(1)
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def is_empty(self):
        # Check if queue empty - O(1)
        return len(self.items) == 0

q = Queue()
q.enqueue('A')
q.enqueue('B')
print(f"Dequeue: {q.dequeue}") # A first