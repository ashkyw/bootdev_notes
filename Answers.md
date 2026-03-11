CH 11 # 1:
3

CH 11 # 2:
2

CH 11 # 3:
```py
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True
        parent = None        
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            elif new_node.val == current.val:
                return

        new_node.parent = parent
        if new_node.parent is None:
            self.root = new_node
            return
        
        if parent.val > new_node.val:
            parent.left = new_node
        if parent.val < new_node.val:
            parent.right = new_node
    
```

CH 11 # 4:
2

CH 11 # 5:
1

CH 11 # 6:
```py
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        
        pivot.parent = pivot_parent.parent
        
        if pivot_parent.parent is None:
            self.root = pivot
        else:
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.left = pivot
            elif pivot_parent == pivot_parent.parent.right:
                pivot_parent.right = pivot
        
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        
        pivot.parent = pivot_parent.parent
        
        if pivot_parent.parent is None:
            self.root = pivot
        else:
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.right = pivot
            elif pivot_parent == pivot_parent.parent.left:
                pivot_parent.left = pivot
        
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

        # don't touch below this line

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
```
