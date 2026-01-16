class TreeNode:
    def __init__(self, key):
        self.key = key           # Node's value
        self.left = None         # Smaller values go left
        self.right = None        # Larger values go right

class BST:
    def __init__(self):
        self.root = None         # Start with empty tree
    
    def insert(self, key):
        # ADD new key maintaining BST property - O(log n) avg
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        # RECURSIVE helper - go left if smaller, right if larger
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)      # New leaf on left
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)     # New leaf on right
            else:
                self._insert_recursive(node.right, key)
    
    def search(self, key):
        # FIND key if exists - O(log n) avg
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        # RECURSIVE search - None = not found
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)
    
    def inorder(self, node):
        # PRINT sorted order (left-root-right) - O(n)
        if node:
            self.inorder(node.left)        # Visit left subtree
            print(node.key, end=" ")       # Visit root
            self.inorder(node.right)       # Visit right subtree[file:1]

if __name__ == "__main__":
    bst = BST()

    # Insert test data: 50, 30, 70, 20, 40
    values = [50, 30, 70, 20, 40]
    for val in values:
        bst.insert(val)

    # Test search
    print(f"Search 30: {bst.search(30)}")     # True
    print(f"Search 25: {bst.search(25)}")     # False

    #Test inorder traversal (should print sorted: 20 30 40 50 70)
    print("Inorder traversal: ", end="")
    bst.inorder(bst.root)
    print()