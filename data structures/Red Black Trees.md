# Unbalanced Trees

BST's have a problem. While it's true that on average a `BST` has `O(log(n))` lookups, deletions, and insertions, that fundamental benefit can break down quickly.

If mostly sorted data, or even worse, completely sorted data, is inserted into a binary tree, the tree will be much deeper than it is wide. As you know by now, the Big O complexity of the tree's operations depend entirely on the depth of the tree.

### Unbalanced Tree

[](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/unbalanced%20tree.png)

### Balanced Tree
[](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/balanced%20tree.png)

Notice that both trees are valid BSTs, and both have the same number of nodes. The trouble is, in the unbalanced tree, there are more levels to traverse, bringing the Big O complexity closer to `O(n)` than `O(log(n))`.
