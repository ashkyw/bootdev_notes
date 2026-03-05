# Trees

[Trees](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)) are a widely used data structure that simulate a hierarchical... well... tree structure. That said, they're typically drawn upside down - the "root" node is at the top, and the "leaves" are at the bottom.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/binary%20trees.png)

Trees are kind of like linked lists in the sense that the root node simply holds references to its child nodes, which in turn hold references to their children, but Tree's nodes can have multiple children instead of just one. A generic tree structure has the following rules:

  * Each node has a value and may have a list of "children"
  * Children can only have a single "parent"
