#Queue example
from collections import deque
queue = deque()
queue.append(1)    # enqueue
queue.append(2)
queue.append(3)
print(queue.popleft())  # 1
print(queue)           # deque([2, 3])

#Stack example
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(stack.pop())  # 3
print(stack)        # [1, 2]

#Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # 1 -> 2 -> 3

#Hasmap example
hashmap = {}
hashmap["key1"] = "value1"  # insert
hashmap["key2"] = "value2"
print(hashmap.get("key1"))  # value1
print("key3" in hashmap)    # False
print("key2" in hashmap)    # True
del hashmap["key1"]
print(hashmap)              # {'key2': 'value2'}
