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

Next step of the linked list:

```py
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)
```

Linked List adding item to the tail of the list:
```py
from node import Node

class LinkedList:
    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for i in self:
            last_node = i
        last_node.next = node
            
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
```
### Some extra info on linked lists

### Classes and Composition

One important distinction: `LinkedList` does **not** inherit from `Node`. Instead, it uses composition.

* A `Node` is a simple container for data and a pointer.
* A `LinkedList` is a manager that holds a reference to the first `Node` (`self.head`).
* Because the `LinkedList` manages `Node` objects, and those objects have a `.next` attribute, you can access that attribute on any node you find while traversing the list.

### How the `for` loop and `yield` work

You hit the nail on the head! Because you defined the `__iter__` method using `yield`, the `LinkedList` becomes an "iterable" object.

1. When you write `for i in self:`, Python calls your `__iter__` method.
2. Inside `__iter__`, the `while` loop starts at `self.head`.
3. Each time it hits `yield` node, it "gives" that node to the `for` loop variable `i`.
4. The `for` loop body runs (`last_node = i`).
5. Then, the `__iter__` method resumes right where it left off, moving to `node.next`.

By the time the `for` loop finishes, `i` (and thus `last_node`) is left holding the very last node that was yielded—the tail of your list.

### The Final Connection

Once the loop is done and you have a reference to the actual tail node in memory, `last_node.next = node` physically connects that old tail to your new node.

Adding to head functionality:

```py
from node import Node

class LinkedList:
    def add_to_head(self, node):
        node.next = self.head
        self.head = node
        return

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            return
        last_node = None
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
```

### Linked List Queue

To use our Linked List as a fast queue `(O(1)` pushes and pops) we need our `add_to_tail` function to be `O(1)`. Currently, it iterates over the entire list before appending an item. We can fix this by *keeping* track of the last item with a new data member: `tail`.

*Note: It's common in algorithms to make this kind of trade-off. By using a little extra memory (keeping track of `tail`), we can make our operations faster. Sometimes you might need to go the other way, and use more computation time to save memory.*

```py
from node import Node

class LinkedList:
    def add_to_head(self, node):
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

```
### Remove from Head

We're one method away from having a fully functioning `O(1)` Queue! We just need a way to remove the first element from the linked list in constant time. When we're finished, our `LinkedList` will fulfill the basic requirements of a Queue:

* `add_to_tail`: Constant time insert
* `remove_from_head`: Constant time pop

Let's rename the `LinkedList` class to `LLQueue` and remove the `add_to_head` functionality because Queues don't allow inserting into the wrong end.

```py
from node import Node

class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        temp.set_next(None)
        return temp

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)
```
