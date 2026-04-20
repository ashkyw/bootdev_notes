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

Another example of  BFS

```py
def bfs_traversal(graph, start):
    if start not in graph:
        return []

    visited = []
    seen = set([start])
    queue = [start]
    index = 0

    while index < len(queue):
        node = queue[index]
        index += 1
        visited.append(node)

        neighbors = graph.get(node, [])
        for neighbor in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited

```
### Complete graphs:

A complete graph is a graph where every pair of vertices is connected by an edge.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/complete_graph.png)

The formula for the number of edges in a complete graph is `n(n - 1)/2`, where `n` is the number of vertices.

# Depth First Search (DFS):

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/dfs.png)

Depth-first search (DFS) is just another algorithm to traverse a graph - kind of like breadth first search. It starts at a root node (some arbitrary node on the graph) and explores as far as possible along each branch before backtracking and starting down the next branch.

Example of DFS in Python:

```py
class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                    self.depth_first_search_r(visited, neighbor)

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

# DFS vs. BFS

So, should you use DFS or BFS when traversing a graph? Well, it depends. Let's look at some rules of thumb we can use to help make the decision.

### Is the Solution Close to the Root?

If you have a good reason to believe the vertex you're looking for is close to the root (where you plan to start searching) then BFS should be faster.

### Does the Graph Have Wide Levels?

Imagine a tree-like graph with `10` vertices on the first level. Each of those ten vertices point to another ten vertices. The number of vertices at each level would be:

    level 0: 1
    level 1: 10
    level 2: 100
    level 3: 1000
    level 4: 10000

Because BFS stores each horizontal level in memory at the same time, you might run out of memory. DFS would likely be more memory efficient.

### Is the Search Space Infinite?

In some searches, the graph has infinite size. For example, imagine a simulation of a game of chess.

The first level of the graph represents all the possible current moves, the next level all the possible 2nd moves, and this goes on forever, especially when you consider that there are possible loops within the game (moving a queen back and forth).

In these cases, true DFS is practically impossible, you would either be forced to:

* Use BFS
*  Use another algorithm
*   Put a limit on how far your DFS algorithm can search before returning

