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

### Iterating

Even though iterating with linked lists is more challenging when compared to the simplicity of normal arrays (or lists) it is a necessity. Despite the implementation being more complex and slow, we can make it easy for users of our class by using the [__iter__](https://docs.python.org/3/reference/datamodel.html#object.__iter__) method.

### `yield` keyword

The [`yield`](https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-yield_stmt) keyword in Python returns a value, similar to `return`. However, it's used to turn a function into a [generator function](https://docs.python.org/3/glossary.html#term-generator). 
Generator functions create a new function object. When *that* function is called, it executes the code in the generator function until it hits a `yield` statement. Here the function pauses and returns the value of the `yield` statement. Next time the function is called it starts where it left off.

```py
def create_message_generator():
    yield "hi"
    yield "there"
    yield "friend"

gen = create_message_generator()
first = next(gen)
print(first)  # prints: hi
second = next(gen)
print(second)  # prints: there
third = next(gen)
print(third)  # prints: friend
```

In the above, everytime the `create_message_generator` function is called it creates a new generator instange .To continue from where you left off, you need to assign the generator to a variable (gen in the example above). When you start using `next()`, or loop over the generator, you continue using the same instance rather than starting a new one.
