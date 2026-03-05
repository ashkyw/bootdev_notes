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
