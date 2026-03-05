# Trees

[Trees](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)) are a widely used data structure that simulate a hierarchical... well... tree structure. That said, they're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/binary%20trees.png)

Trees are kind of like linked lists in the sense that the root node simply holds references to its child nodes, which in turn hold references to their children, but Tree's nodes can have multiple children instead of just one. A generic tree structure has the following rules:

  * Each node has a value and may have a list of "children"
  * Children can only have a single "parent"

### Binary Trees

Trees aren't particularly useful data structures unless they're ordered in some way. One of the most common types of ordered tree is a [Binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree) or `BST`. A `BST` has some additional constraints:

1, Instead of an unbounded list of children, each node has *at most* 2 children
2. The left child's value must be *less than* its parent's value
3. The right child's value must be *greater than* its parent's value
4. No two nodes in the `BST` can have the same value

By ordering the tree like this, we can traverse the tree to find the node we want much faster.

Start of creating a BST tree with insert function:

```py
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

```
