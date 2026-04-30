from RBTree import RedBlackTree

# Create a new tree
tree = RedBlackTree()

# Insert values
tree.insert(10)
tree.insert(20)
tree.insert(5)

# Search for values
if tree.find(10):
    print("Value 10 found!")

# Traverse and display tree
tree.traverse()  # Prints: [5 (Black)] [10 (Black)] [20 (Red)]

# Delete values
tree.delete(10)