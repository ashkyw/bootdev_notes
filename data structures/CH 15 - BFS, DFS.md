# Breadth First Search (BFS)

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at a root (some arbitrary node on a graph), and explores all of the neighbor nodes _at the present depth_ before going on to the nodes at the next level.

**[BFS Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Breadth-first-search-1920x1080.mp4)**

### Stable Sorting

Non-integer sets are _not_ "stable" in Python - the order of elements in a set is not guaranteed to be the same each time you iterate over it.

While testing, we want our algorithm to search the _same way every time_ to make debugging easier. Python offers a `sorted()` function we can call on our `set()` that will return a sorted iterable.

```py
sorted_items = sorted(unsorted_set)
```
