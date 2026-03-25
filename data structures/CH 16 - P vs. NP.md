# NP

![Video Link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/np-1920x1080.mp4)

[Nondeterministic polynomial time](https://en.wikipedia.org/wiki/NP_(complexity)), `NP`, is the set of problems whose solutions can be _verified_ in [polynomial time](https://en.wikipedia.org/wiki/Time_complexity#Polynomial_time), but not necessairly _solved_ in polynomial time.

### P is in NP

Becuse all problems that can be _solved_ in polynomial time can also be _verified_ in polynomial time, all the problems in `P` are also in `NP`

### The Oracle

A good way of thinking about problems in `NP` is to imagine that we have a magic oracle that gives us potential solutions to problems. Here would be our process for finding if a problem is in `NP`:
  * Present the problem to the magic oracle
  * The magic oracle gives us a potential solution
  * We verify in polynomial time that the solution is correct

If we can do the verification in polynomial time, the problem is in `NP`, otherwise, it isn't.

### Traveling Salesman Problem

A famous example of a problem in `NP` is the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem), also known as `TSP`,

The version of the problem that we will solve can be stated!

        Given a list of cities, the distances between each pair of cities, and a total distance, 
        is there a path through all the cities that is less than the distance given?

  ![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/traveling%20salesman%20problem.png)

  For example, with the above graph, the problem could be, "Is there any way to travel through A, B, C, and D in less than a distance of `67`? The answer would be "yes" by way of `A→B→D→C`

Brute force solution to TSP:

  ```py
def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res

def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
```
