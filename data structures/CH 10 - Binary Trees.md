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

### Insert Review

Inserting into a binary search tree (like most of its operations) is very fast. Picture the algorithm above in your head: how many comparisons does it take to find the right spot for a new node?

It only requires one comparison for each level of the tree, making it `O(log(n))`! (At least in a balanced tree.

Order `log(n)` is very fast - it's practically as good as `O(1)` in most cases. If our tree has 1,000,000 nodes, we only need to make 20 comparisons to find the right spot for a new node. If our tree is 2x larger (2,000,000 nodes), we only need to make one more comparison per insert, 21 total.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/binary%20search%20big%20o.png)

Adding get_min, get_max to BST:
```py
class BSTNode:
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

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

### Deletion Review

The delete method is O(log(n)) because, like most binary tree operations, we don't have to search the entire tree. We only have to search one path from the root to the leaf node we want to delete.

The depth of the tree on average is equal to log base 2 of the number of nodes in the tree. For example:
|Nodes |	Depth |
|------|------|
| 1 |	0 |
| 2 |	1 |
| 4 |	2 |
| 8 |	3 |
| 16 |	4 |
| 32 |	5 |
| 64 |	6 |
| 128 |	7 |
| 256 |	8 |
| 512 |	9 |
| 1024 |	10 |
| 2048 |	11 |
| 4096 |	12 |

We only need to use ~10 steps to delete a node from a tree of ~1000 nodes.

Adding delete function to BST:

```py
class BSTNode:
    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

```
