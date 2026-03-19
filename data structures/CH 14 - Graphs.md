# Graphs

A [graph](https://en.wikipedia.org/wiki/Graph_%28discrete_mathematics%29) is a set of vertices and the edges that connect those vertices. _All trees are graphs, but not all graphs are trees._

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/graphs.png)

For now, we'll use a matrix to represent the edges in a graph that connect each pair of vertices. For example, here's a matrix that represents the graph above.

| 0 | 1 | 2 | 3 | 4 |
|----|---|---|----|---|
| 0 | False | True | False | False | True |
| 1 | True | False | True | True | True |
| 2 | False | True | False | True | False |
| 3 | False | True | True | False | True |
| 4 | True | True | False | True | False |

In python, we can use a list of lists to represent this matrix:

```py
[
  [False, True, False, False, True],
  [True, False, True, True, True],
  [False, True, False, True, False],
  [False, True, True, False, True],
  [True, True, False, True, False]
]
```
In any `True` cell the corresponding vertices are connected by an edge.

Setting up graph matrix:

```py
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = []
        for num in range(int(self.num_vertices)):
            self.graph.append([False for i in range(int(self.num_vertices))])
    
    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]
```
