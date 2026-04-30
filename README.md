# Red-Black Tree Implementation

A complete implementation of a Red-Black Tree data structure in Python, including insertion, deletion, and search operations with comprehensive test coverage.

## Overview

This project implements a Red-Black Tree. A Red-Black Tree is a type of balanced BST where each node is colored either red or black, ensuring O(log n) time complexity for insertions, deletions, and searches.

**Red-Black Tree Properties:**

1. Every node is either red or black
2. The root is black
3. All leaves (NIL nodes) are black
4. Red nodes cannot have red children
5. All paths from a node to its leaves contain the same number of black nodes

## Design Decisions

- **No Duplicate Values**: The implementation prevents duplicate values from being inserted
- **NIL Nodes**: Leaf nodes are represented by NIL nodes (TreeNode with no value and black coloring)
- **node.black**: Because all nodes must be red or black, color is represented as a binary value.
- **node.parent**: For ease of traversal, each node stores a reference to their parent (None for root)

## Preformance Analysis

### Search (find)

Like a standard BST, search recurses through the height of the tree, and each recursion is constant time (c). Because Red-Black Trees have guarenteed height `h <= 2\*log(n+1)`, the search function is, at worst, **O(log(n))**.

### Insertion

Finding the insertion location of the node requires a search call, which takes O(log(n)) time. After the node is inserted, fixing the coloring of the tree can recurse up the height of the tree, with each call taking c time. Because of this, at worst, `T(n) = O(log(n)) + c*(2*log(n+1)) = O(log(n))`. Similarly, at best, there is no coloring fixes required, and `T(n) = O(log(n)) + c = O(log(n))`. Because best and worse case complexity are the same, average complexity is also **O(log(n))**.

### Deletion

Deletion requires a search call to locate the node to delete, which is already O(log(n)). Additionally, similar to search, delete can recurse all the way up the height of the tree, with each recursion taking c time. At worst, if delete recurses all the way to the root node, `T(n) = O(log(n)) + c*(2*log(n+1)) = O(log(n))`. At best, deletion does not recurse, and just takes constant time, `T(n) = O(log(n)) + c = O(log(n))`. Because best and worse case complexity are the same, average complexity is also **O(log(n))**.

### Summary and Comparison

Like AVL Trees, Red-Black Trees are self-balancing and guarentee the O(log(n)) time complexity, regardless of input. Standard BSTs are not self balancing, so at worst they can become unbalanced and lose their log(n) time complexity. However, to ensure this, Red-Black Trees require a lot of additional logic and complexity, so there are certainly some drawbacks to using this data structure.

**Red-Black Tree**
| Operation | Average | Worst Case |
| --------- | -------- | ---------- |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Search | O(log n) | O(log n) |

**AVL Tree**
| Operation | Average | Worst Case |
| --------- | -------- | ---------- |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |
| Search | O(log n) | O(log n) |

**BST**
| Operation | Average | Worst Case |
| --------- | -------- | ---------- |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Search | O(log n) | O(n) |

## Files

### RBTree.py

Core implementation of the Red-Black Tree with two main classes:

#### `TreeNode`

A single node in the tree.

- **Attributes:**
  - `val`: The value stored in the node (None for NIL nodes)
  - `black`: Boolean value for color (True = Black, False = Red)
  - `left`: Reference to left child
  - `right`: Reference to right child
  - `parent`: Reference to parent node

- **Methods:**
  - `sibling()`: Returns the sibling node

#### `RedBlackTree`

Main class managing the tree structure and operations.

**Helper Methods:**

- `setParent(n)`: Finds and sets the parent of a given node
- `rotateRight(x)`: Performs a right rotation about node x
- `rotateLeft(x)`: Performs a left rotation about node x
- `BSTFindNew(n)`: Finds the replacement node for deletion
- `insertColorFix(n)`: Repairs tree coloration after insertion
- `fixDoubleBlack(x)`: Repairs tree coloration after deletion
- `findPointer(val)`: Returns reference to node with specified value

**Main Operations:**

- `insert(value)`: Inserts a new value into the tree
  - Creates new node with red color
  - Calls `insertColorFix()` to restore properties
  - Time complexity: O(log n)
- `delete(val)`: Removes a value from the tree
  - Asserts value exists in tree
  - Recursively reduces to leaf deletion
  - Calls `fixDoubleBlack()` if needed for black node removal
  - Time complexity: O(log n)
- `find(val, n)`: Searches for a value in the tree
  - Returns True if found, False otherwise
  - Time complexity: O(log n)
- `traverse(n, res)`: Traverses the tree (In-Order)
  - Prints nodes with their colors
  - Returns dictionary of values and their colors

### RBTreeTest.py

Test suite with 16 test cases covering:

**Validation Helper Functions:**

- `isValidRBTree(t)`: Checks if tree satisfies all Red-Black properties
- `checkNodes(n)`: Validates BST structure and color constraints
- `checkBH(n, bh, cur)`: Verifies black-height property

**Test Categories:**

1. **Tree Initialization** (Test 1)
   - Validates empty tree

2. **Insertion Tests** (Tests 2-5)
   - Single insertion
   - Dual insertion
   - Sequential insertion (1-29)
   - Reverse sequential insertion (30-1)

3. **Search/Find Tests** (Tests 6-9)
   - Search in empty tree
   - Search for non-existent values
   - Search for single value
   - Search for multiple values

4. **Traversal Tests** (Tests 10-12)
   - Empty tree traversal
   - Single node traversal
   - Multi-node traversal

5. **Deletion Tests** (Tests 13-16)
   - Deletion of single node
   - Deletion of first node in two-node tree
   - Complete deletion of all nodes
   - Multiple deletions in large tree

## Usage

```python
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
tree.traverse()  # Prints: [5 (Red)] [10 (Black)] [20 (Red)]

# Delete values
tree.delete(10)
```

## Running Test Suite

Execute the test suite:

```bash
python RBTreeTest.py
```

This will display the number of passing tests out of 16 total.
