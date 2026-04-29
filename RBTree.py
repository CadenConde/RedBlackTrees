# TreeNode datatype:
# Single node of a tree, black and NIL by default, unless otherwise defined
# TreeNode.val stores the value of the node, NIL by default
# TreeNode.black is a binary value, T = Black, F = Red.
# TreeNode.left and TreeNode.right store the child nodes.
# TreeNode.parent points to the parent node.

class TreeNode:
    # basic constructor
    def __init__(self, val=None, black=True):
        self.val = val
        self.black = black
        self.left = None
        self.right = None
        self.parent = None
        
    # Sibling helper method returns sibling of node
    def sibling(self):
        assert self.parent, "Root node has no sibling"
        p = self.parent
        if self == p.left:
            return p.right
        else:
            return p.left
        
        
class RedBlackTree:
    # constructor, sets root to new NIL node unless otherwise provided
    def __init__(self, root=TreeNode()):
        self.root = root
    
    # ------------------------- Helper methods --------------------------
    
    # sets the n.parent for node n in the tree
    def setParent(self, n):
        assert n.val, "Node must have a value"
        prev = None
        next = self.root
        while next and next.val:
            assert not next.val == n.val, "Repeat values not allowed."
            prev = next
            if next.val > n.val:
                next = next.left
            else:
                next = next.right
        n.parent = prev
    
    # rotate right about node x
    def rotateRight(self, x):
        self.traverse()
        y = x.left # promoted node
        
        # switch subtrees
        temp = y.right 
        y.right = x
        x.left = temp
        y.parent = x.parent
        
        # link parents
        if not x.parent: 
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        x.parent = y
        
    # rotate left about node x
    def rotateLeft(self, x):
        y = x.right # promoted node
        
        # switch subtrees
        temp = y.left 
        y.left = x
        x.right = temp
        y.parent = x.parent
        
        # link parents
        if not x.parent: 
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        x.parent = y
        
    # --------------------------- Main methods --------------------------
        
    # insert node n into tree
    def insert(self, value):
        #initalize node with 2 NIL children
        n = TreeNode(val=value)
        n.left = TreeNode()
        n.right = TreeNode()
        
        self.setParent(n)
        if n.parent == None:
            self.root = n
        elif n.parent.val > n.val:
            n.parent.left = n
        else:
            n.parent.right = n
        n.black = False # set n's color to red
        self.insertColorFix(n)
        print()
        
    # fix coloring after insertion
    def insertColorFix(self, n):
        while not n == self.root and not n.parent.black:
            # Case 1: parent and uncle both red.
            if n.parent.sibling().black == False:
                n.parent.black = True # set parent black
                n.parent.sibling().black = True # set uncle black
                
                n = n.parent.parent # set n = grandparent, check again
                n.black = False # set grandparent as red
            
            # Case 2-3: uncle is black
            else:
                # Case 2: left of grandparent
                if n.parent == n.parent.parent.left:
                    g = n.parent.parent # grandparent
                    if n.parent == n.parent.right: # Case 2a: left-right of grandparent
                        self.rotateLeft(n.parent)
                    self.rotateRight(g)
                    g.parent.black = True
                    g.black = False
                    
                # Case 3: right of grandparent
                else:
                    g = n.parent.parent # grandparent
                    if n.parent == n.parent.left: # Case 3a, right-left of grandparent
                        self.rotateRight(n.parent)
                    self.rotateLeft(g)
                    g.parent.black = True
                    g.black = False
        self.root.black = True # ensure root remains black
        
    # traverse and print values through the tree
    # search from root by default
    def traverse(self, n=None):
        if not n:
            n = self.root
        if n.val:
            self.traverse(n.left)
            
            color = "Black"
            if not n.black:
                color = "Red"
            if n.parent:
                print(f"[{n.val} ({color}) (parent = {n.parent.val})]", end=" ")
            else:
                print(f"[{n.val} ({color}) (Root Node)]", end=" ")
                
            self.traverse(n.right)
   
    # find value in the tree, "True" if present, false otherwise         
    def find(self, val, n=None):
        # start searching from root unless otherwise defined
        if not n: 
            n = self.root
        # NIL Node
        if not n.val:
            return False
        if n.val == val:
            return True
        elif n.val > val:
            return self.find(val, n.left)
        else:
            return self.find(val, n.right)
            
    # find value in the tree, "True" if present, false otherwise         
    def findPointer(self, val, n=None):
        # start searching from root unless otherwise defined
        if not n: 
            n = self.root
        if n.val == val:
            return n
        elif n.val > val:
            return self.findPointer(val, n.left)
        else:
            return self.findPointer(val, n.right)
            
    # removes a node v from the tree, must only delete leaf nodes so recurses to a leaf node if v is not a leaf node
    def delete(self, val):
        assert self.find(val), "Value must exist in the tree"
        v = self.findPointer(val)
        u = self.BSTFindNew(v)
        
        # v is a leaf
        if not u.val:
            if v == self.root:
                self.root = TreeNode()
            else: 
                # if v is black, verify black property not violated (double black)
                if v.black:
                    self.fixDoubleBlack(v) # todo
                # if v is red, just remove
                if v.parent.left == v:
                    v.parent.left = TreeNode()
                else:
                    v.parent.right = TreeNode()
                    
        # v has 1 child
        elif not v.left.val or not v.right.val:
            if v == self.root:
                self.root = u
                u.parent = None
                u.black = True
            else:
                if v.parent.left == v:
                    v.parent.left = u
                else:
                    v.parent.right = u
                u.parent = v.parent
                if u.black and v.black:
                    self.fixDoubleBlack(u)
                else:
                    u.black = True
            return
        # v has 2 children, swap values and remove u
        else:
            temp = u.val
            # this is technically recursive, but u is guarenteed to have 1 or 0 children, so it can only possibly recurse once
            self.delete(u.val)
            v.val = temp
            
    def fixDoubleBlack(self, x):
        # double black root is just single blakc
        if x == self.root:
            return
        
        # no sibling, push up further
        if not x.sibling().val:
            self.fixDoubleBlack(x.parent)
        else:
            # sibling is red
            if not x.sibling().black:
                x.parent.black = False
                x.sibling().black = True
            
                if x.parent.left == x.sibling():
                    self.rotateRight(x.parent)
                else:
                    self.rotateLeft(x.parent)
                self.fixDoubleBlack(x)
                
            else:
                #sibling is black
                if not x.sibling().left.black or not x.sibling().right.black:
                    if x.sibling().left.val and not x.sibling().left.black:
                        #left left
                        if x.parent.left == x.sibling():
                            x.sibling().left.black = x.sibling().black
                            x.sibling().black = x.parent.black
                            self.rotateRight(x.parent)
                        #right left
                        else:
                            x.sibling().left.black = x.parent.black
                            self.rotateRight(x.sibling())
                            self.rotateLeft(x.parent)
                    else:
                        #left right
                        if x.parent.left == x.sibling():
                            x.sibling().right.black = x.parent.black
                            self.rotateLeft(x.sibling())
                            self.rotateRight(x.parent)
                        #right right
                        else:
                            x.sibling().right.black = x.sibling().black
                            x.sibling().black = x.parent.black
                            self.rotateLeft(x.parent)
                     
                # 2 black children       
                else:
                    x.sibling().black = False
                    if x.parent.black:
                        self.fixDoubleBlack(x.parent)
                    else:
                        x.parent.black = True
                        
    # return the node n will be replaced with
    def BSTFindNew(self, n):
        # return sole child if only 1, or NIL node if 0
        if not n.right.val:
            return n.left
        elif not n.left.val:
            return n.right
        
        # find replacement node if has 2 children
        if n.left.val and n.right.val:
            x = n.right
            while x.left.val:
                x = x.left
            return x 
        
        