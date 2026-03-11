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
