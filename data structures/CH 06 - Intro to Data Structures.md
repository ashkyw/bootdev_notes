# Introduction to Data Structures

Starting with this chapter, we're going to focus on how we can store and organize data in a way that allows for even *better* algorithms.

Data structures are just organizational tools that allow for more advanced algorithms. Some examples:

* **Stacks**: Last in, first out.
* **Queues**: First in, first out.
* **Linked Lists**: A chain of nodes, efficient for inserts and deletes.
* **Binary Trees**: A tree where each node has up to two children.
* **Red Black Trees**: A self-balancing binary tree using colors.
* **Hashmaps**: A data structure that maps keys to values.
* **Tries**: A tree used for storing and searching words efficiently.
* **Graphs**: A collection of nodes connected by edges.

### What Are Data Structures?

A data structure is a data organization, management, and storage format that enables efficient access and modification. 
More precisely, a data structure is a collection of data values, the relationships among them, and the functions or 
operations that can be applied to the data.

### In other words, a data structure:

* Stores data
* Organizes data so that it can easily be accessed and modified
* Contains algorithmic functions to expose the ability to read and modify the data

# Lists

Okay, we know what lists are, but from a data structures and algorithms perspective, what are they good for? Let's break it down by operation:

* **Append**: Appending an element to the end of a list, e.g. `cars.append("ford")` is (on average) `O(1)`. We go directly to the end and add the element.
* **Index**: Accessing an element by index, e.g. `cars[2]` is `O(1)`. We go directly to the index and return the element.
* **Delete**: Removing an element from the middle of a list, e.g. `cars.pop(2)` is `O(n)`. We have to shift all the elements after the deleted element down one index.
* **Search**: Searching for an element in a list, e.g. `cars.index("ford")` is `O(n)`. We have to iterate over the list until we find the element.

In other words, lists start to struggle in two primary areas:

1. When you need to frequently delete elements from the middle of the list
2. When you need to frequently search for specific elements in the entire list
