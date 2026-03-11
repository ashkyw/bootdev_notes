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

>The "red" and "black" nomenclature is arbitrary - you could call them "red vs blue" trees >(shout-out rooster teeth), or not even call it "color" at all. The important part is just that we >now have two "types" of nodes and that will affect the algorithm for balancing it.

List of Very Simple Rules

  * Each node is either red or black,
  * The root is black.
  * All Nil leaf nodes are black.
  * If a node is red, then both its children are black.
  * All paths from a single node go through the same number of black nodes to reach any of its descendant Nil (black) nodes.

As it turns out, we've been inserting user records into our tree with incrementing numerical IDs (pre sorted data)! The app's user lookups are starting to get really slow. Let's start implementing a Red-Black tree to speed things up.

In a normal BST, the child nodes don't need to know about, or carry a reference to their parent. The same is not true for Red-Black trees.
