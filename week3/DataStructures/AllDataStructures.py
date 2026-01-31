from stack import Stack
from queue import Queue
from linkedlist import LinkedList
from hashmap import HashMap
from bst import BST

if __name__ == "__main__":
    print(" TESTING ALL DATA STRUCTURES ")
    
    # Stack test
    s = Stack()
    s.push(1); s.push(2)
    assert s.peek() == 2, "Stack peek failed"
    assert s.pop() == 2, "Stack pop failed"
    
    # Queue test
    q = Queue()
    q.enqueue('A'); q.enqueue('B')
    assert q.dequeue() == 'A', "Queue order failed"
    
    # LinkedList test
    ll = LinkedList()
    ll.insert(10); ll.delete(10)
    assert ll.head is None, "LinkedList delete failed"
    
    # HashMap test
    hm = HashMap()
    hm.insert("key", "value")
    assert hm.search("key") == "value", "HashMap search failed"
    
    # BST test
    bst = BST()
    bst.insert(50); bst.insert(30)
    assert bst.search(50) == True, "BST search failed"
    
    print(" ALL TESTS PASSED!")
