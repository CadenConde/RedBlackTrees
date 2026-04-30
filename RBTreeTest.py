from RBTree import RedBlackTree


# ------------------- helper methods ---------------------
def isValidRBTree(t):
    n = t.root
    
    # empty tree
    if not n.val and n.black:
        return True
    
    # ensure root is black and RBTree properties are fulfilled
    valid = n.black and checkNodes(n.left) and checkNodes(n.right)
    
    # find bh of a single leaf
    bh = 0
    while n.val:
        if n.black:
            bh += 1
        n = n.left
        
    # recursively check tree for bh property
    valid = valid and checkBH(t.root, bh, 0)
    return valid

def checkBH(n, bh, cur):
    # leaf has correct bh
    if not n.val and bh == cur:
        return True
    # leaf has incorrect bh
    elif not n.val and bh != cur:
        return False
    # recurse further
    else:
        if n.black:
            return checkBH(n.left, bh, cur+1) and checkBH(n.right, bh, cur+1)
        else:
            return checkBH(n.left, bh, cur) and checkBH(n.right, bh, cur)

def checkNodes(n):
    if not n.val:
        # black NIL nodes
        if not n.black:
            return False
        return True
    
    # no adjacent reds
    if not n.black and not n.parent.black:
        return False
    
    # must have 2 children
    if not n.left or not n.right:
        return False
    
    # BST Structure
    if n.parent.left == n:
        if n.val > n.parent.val:
            return False
    else:
        if n.val < n.parent.val:
            return False
    
    return checkNodes(n.left) and checkNodes(n.right)

# -------------------------------------------------------------
# -                        Test Cases                         -
# -------------------------------------------------------------


passed = 0
total = 16

# ------------------------ Tree Test --------------------------
t = RedBlackTree()
assert isValidRBTree(t), "Failed Test 1"
if isValidRBTree(t):
    passed += 1
    

# ------------------------ Insertion Tests --------------------
t = RedBlackTree()
t.insert(10)
assert t.find(10) and isValidRBTree(t), "Failed Test 2"
if t.find(10) and isValidRBTree(t):
    passed += 1

t = RedBlackTree()
t.insert(20)
t.insert(10)
assert t.find(10) and t.find(20) and isValidRBTree(t), "Failed Test 3"
if t.find(10) and t.find(20) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
for i in range(1, 30):
    t.insert(i)
foundAll = True
for i in range(1, 30):
    foundAll = foundAll and t.find(i)
assert foundAll and isValidRBTree(t), "Failed Test 4"
if foundAll and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
for i in range(30, 1, -1):
    t.insert(i)
foundAll = True
for i in range(30, 1, -1):
    foundAll = foundAll and t.find(i)
assert foundAll and isValidRBTree(t), "Failed Test 5"
if foundAll and isValidRBTree(t):
    passed += 1
    
# ------------------------ Find (Search) Tests --------------------

t = RedBlackTree()
assert not t.find(10) and not t.find(0) and isValidRBTree(t), "Failed Test 6"
if not t.find(10) and not t.find(0) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(12)
assert not t.find(10) and not t.find(0) and isValidRBTree(t), "Failed Test 7"
if not t.find(10) and not t.find(0) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(12)
assert t.find(12) and isValidRBTree(t), "Failed Test 8"
if t.find(12) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(12)
t.insert(13)
t.insert(14)
t.insert(15)
assert not t.find(11) and t.find(12) and t.find(13) and t.find(14) and t.find(15) and not t.find(16) and isValidRBTree(t), "Failed Test 9"
if not t.find(11) and t.find(12) and t.find(13) and t.find(14) and t.find(15) and not t.find(16) and isValidRBTree(t):
    passed += 1
    
# ------------------------ Traverse Tests --------------------
# Traverse Prints and returns a dictionary of nodes encountered and their colors, 
# and prints output, this just checks the dictionary is what is expected

t = RedBlackTree()
expected = {}
assert t.traverse() == expected and isValidRBTree(t), "Failed Test 10"
if t.traverse() == expected and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(1)
expected = {}
expected[1] = "Black"
assert t.traverse() == expected and isValidRBTree(t), "Failed Test 11"
if t.traverse() == expected and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
expected = {}
expected[1] = "Black"
expected[2] = "Black"
expected[3] = "Black"
expected[4] = "Red"
assert t.traverse() == expected and isValidRBTree(t), "Failed Test 12"
if t.traverse() == expected and isValidRBTree(t):
    passed += 1

# ------------------------ Deletion Tests --------------------
t = RedBlackTree()
t.insert(10)
t.delete(10)
assert not t.find(10) and isValidRBTree(t), "Failed Test 13"
if not t.find(10) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(10)
t.insert(20)
t.delete(10)
assert not t.find(10) and t.find(20) and isValidRBTree(t), "Failed Test 14"
if not t.find(10) and t.find(20) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
t.insert(10)
t.insert(20)
t.delete(20)
t.delete(10)
assert not t.find(10) and not t.find(20) and isValidRBTree(t), "Failed Test 15"
if not t.find(10) and not t.find(20) and isValidRBTree(t):
    passed += 1
    
t = RedBlackTree()
for i in range(1, 30):
    t.insert(i)
t.delete(20)
t.delete(25)
assert not t.find(20) and not t.find(25) and isValidRBTree(t), "Failed Test 16"
if not t.find(20) and not t.find(25) and isValidRBTree(t):
    passed += 1

# fancy screen clearing stuff
print("\033[H\033[J", end="")

print(f"[{passed}/{total} Tests Pass]")
