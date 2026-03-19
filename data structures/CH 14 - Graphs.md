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
