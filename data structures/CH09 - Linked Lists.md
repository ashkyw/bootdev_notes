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

### Linked List vs List

A linked list is a collection of ordered items, so it's similar to a "normal" list (also known as an "array" or "slice" in other languages).

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/list%20vs%20linked%20list.png)

Items in a "normal" list are stored next to each other in memory. To get an item from a `list` we have to use a numbered index. 

```py
car = cars[3]
```

An index can be thought of as simply an offset from the start. The `cars` list above refers to the start of the list, and `3` is just the 4th item in that section of memory. In normal lists, all data is stored in the same place in memory, and the index is just a way to find the right spot.

```py
current_car_node = head_car_node
while current_car_node is not None:
    print(current_car_node.val)
    current_car_node = current_car_node.next
```

Linked lists can be annoying to use, and incur more overhead. So, *why* do we use them? *Sometimes* linked lists are much faster to make updates to, *particularly when inserting or deleting items from the middle*.

In a normal list, if you insert an item in the middle, you have to shift *all* the items after it down one spot, which takes `O(n)` time.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/list%20manipulation.png)

In a linked list once you've traversed to a given node insertion is `(O(1))` because you simply update two references.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/linked%20list%20manipulation.png)
