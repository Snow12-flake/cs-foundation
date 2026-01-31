class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1); q.enqueue(2)
    print(q.dequeue())  # 1

