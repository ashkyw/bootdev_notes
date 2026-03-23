# Breadth First Search (BFS)

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at a root (some arbitrary node on a graph), and explores all of the neighbor nodes _at the present depth_ before going on to the nodes at the next level.

**[BFS Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Breadth-first-search-1920x1080.mp4)**

### Stable Sorting

Non-integer sets are _not_ "stable" in Python - the order of elements in a set is not guaranteed to be the same each time you iterate over it.

While testing, we want our algorithm to search the _same way every time_ to make debugging easier. Python offers a `sorted()` function we can call on our `set()` that will return a sorted iterable.

```py
sorted_items = sorted(unsorted_set)
```

Example of BFS in Python:

```py
class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
```

### Complete graphs:

A complete graph is a graph where every pair of vertices is connected by an edge.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/complete_graph.png)

The formula for the number of edges in a complete graph is `n(n - 1)/2`, where `n` is the number of vertices.
