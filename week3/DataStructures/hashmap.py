from Linkedlist import LinkedList
class HashMap:
    def __init__(self, size=10):
        # Create 'size' buckets, each a LinkedList for chaining
        self.size = size
        self.buckets = [LinkedList() for _ in range(size)]
    
    def hash_key(self, key):
        # CONVERT key to bucket index (0 to size-1) - O(1)
        return hash(key) % self.size
    
    def insert(self, key, value):
        # PUT key-value pair in correct bucket - O(1) avg
        index = self.hash_key(key)
        # Store as tuple (key, value) in linked list at bucket
        self.buckets[index].insert((key, value))
    
    def search(self, key):
        # FIND value by key - O(1) avg, O(n) worst
        index = self.hash_key(key)
        current = self.buckets[index].head
        while current:
            if current.data[0] == key:  # Found matching key
                return current.data[1]   # Return value
            current = current.next
        return None  # Key not found

if __name__ == "__main__":
    hm = HashMap(size=5)
    
    # Test basic insert/search
    hm.insert("name", "Alice")
    hm.insert("age", "30")
    print(f"Search 'name': {hm.search('name')}")  # Alice
    
    # Test collision (same hash bucket)
    hm.insert("game", "chess")  # May collide with "name"
    print(f"Search 'game': {hm.search('game')}")  # chess
    
    # Test overwrite
    hm.insert("name", "Bob")
    print(f"Overwritten 'name': {hm.search('name')}")  # Bob
    
    print(f"Missing key: {hm.search('city')}")  # None

