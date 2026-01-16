class Node:
    def __init__(self, data):
        self.data = data      # Value stored in node
        self.next = None      # Pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of list
    
    def insert(self, data):
        # INSERT at HEAD (beginning) - O(1)
        new_node = Node(data)
        new_node.next = self.head  # New node points to old head
        self.head = new_node       # Head now points to new node
    
    def delete(self, data):
        # DELETE first occurrence of data - O(n)
        if self.head and self.head.data == data:
            self.head = self.head.next  # Remove head
            return
        
        current = self.head
        while current and current.next:
            if current.next.data == data:
                current.next = current.next.next  # Skip node
                return
            current = current.next
    
    def print_list(self):
        # TRAVERSE and print all nodes - O(n)
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.print_list
