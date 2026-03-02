# Linked Lists

A [linked list](https://en.wikipedia.org/wiki/Linked_list) is where the elements of a list are *not* stored next to each other in memory (like a normal list). Instead, each item references the next in a chain.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/linked%20list.png)

Beginning of Linked List in Python:

```py
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    # don't touch below this line

    def __repr__(self):
        return self.val

```

![]()
