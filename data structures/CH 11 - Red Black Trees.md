# Unbalanced Trees

BST's have a problem. While it's true that on average a `BST` has `O(log(n))` lookups, deletions, and insertions, that fundamental benefit can break down quickly.

If mostly sorted data, or even worse, completely sorted data, is inserted into a binary tree, the tree will be much deeper than it is wide. As you know by now, the Big O complexity of the tree's operations depend entirely on the depth of the tree.

### Unbalanced Tree

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/unbalanced%20tree.png)

### Balanced Tree
![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/balanced%20tree.png)

Notice that both trees are valid BSTs, and both have the same number of nodes. The trouble is, in the unbalanced tree, there are more levels to traverse, bringing the Big O complexity closer to `O(n)` than `O(log(n))`.

# Red-Black Tree

A [red-black](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree) tree is a _kind_ of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

### How It Works

Each node in an RB Tree stores an extra bit, called the "color": either red or black. The "color" ensures that the tree remains approximately balanced during insertions and deletions. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

>The "red" and "black" nomenclature is arbitrary - you could call them "red vs blue" trees (shout-out rooster teeth), or not even call it "color" at all. The important part is just that we now have two "types" of nodes and that will affect the algorithm for balancing it.

List of Very Simple Rules

  * Each node is either red or black,
  * The root is black.
  * All Nil leaf nodes are black.
  * If a node is red, then both its children are black.
  * All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.

As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. The same is not true for Red-Black trees.

Beginnings of Red Black Tree:

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

### Rules

In addition to all the rules of a Binary Search Tree, a red-black tree must follow some additional ones:

   1. Each node is either red or black
   2. The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
   3. All `Nil` leaf nodes are black.
   4. If a node is red, then both its children are black.
   5. All paths from a single node go through the same number of black nodes to reach any of its descendant `NIL` nodes.

Perfectly Balanced?

The re-balancing of a red-black tree does not result in a perfectly balanced tree. It only limits how unbalanced a tree may become. However, its insertion and deletion operations, along with the tree rearrangement and recoloring, are always performed in `O(log(n))` time.

### Rotation

"Rotations" are what actually keep a _red-black tree balanced_. Every time one branch of the tree starts to get too long, we will "rotate" those branches to keep the tree shallow. A shallow tree is a healthy (fast) tree!

   * A properly-ordered tree pre-rotation remains a properly-ordered tree post-rotation
   * Rotations are `O(1)` operations
   * When rotating left:
       * The "pivot" node's initial parent becomes its left child
       * The "pivot" node's old left child becomes its initial parent's new right child

Here's the process of a "left rotation":

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/rotation.png)

Adding Rotation functionality:

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
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
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
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

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
