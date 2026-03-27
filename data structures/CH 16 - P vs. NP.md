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

Brute force solution to TSP in `NP`, due to being `O(n!)` time:

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

Easy solution in `P` to verify TSP:

```py
def verify_tsp(paths, dist, actual_path):
    total = 0
    for i in range(len(actual_path)):
        if i != 0:
            total += paths[actual_path[i - 1]][actual_path[i]]
    return total < dist
```

### NP-Complete

Some, but not all problems in `NP` are also [NP-complete](https://en.wikipedia.org/wiki/NP-completeness).

A problem in `NP` is also `NP-complete` if _every_ other problem in `NP` can be [reduced](https://en.wikipedia.org/wiki/Reduction_(complexity)) to it in polynomial time.

### What Does “reduced” Mean?

We won't dive deep into the [subject of reductions](https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/npcomplete.pdf) in this course, but we'll cover the basic idea.

A reducer is an algorithm that transforms some problem, `Problem A`, into a different problem which is already solved, `Problem B`. Then, `Problem A` can be solved with the algorithm for solving `Problem B`.

`Problem A` -> reducer -> `Problem B` -> solver algorithm `Problem B` -> solution for `Problem A`

However, the reducer itself needs to be fast. "Problem A is reducible to Problem B" if the reducer can run in polynomial time.

### So Who Cares?

Well, this means that if we can find an algorithm that solves any of the `NP-complete` problems in polynomial time, then all problems in NP can also be solved in polynomial time.

Super-duper-smart computer scientists have proven it. Trust me. Or optionally [read more about it](https://web.stanford.edu/class/archive/cs/cs103/cs103.1134/lectures/26/Small26.pdf) if you're interested.

### Verifying Solutions

Let's circle back to this idea of "slow to solve, fast to verify".

Even when we aren't specifically talking about P and NP, the concept of "slow to solve, fast to verify" is very important in real-world software. As a trivial example, imagine the password on an email account. When a user inputs a password like:

`p@ssword4Mi`

It's easy to verify if that password matches the one we have saved on file. It's literally as easy as:
```py
should_grant_access = user_input == saved_password
```
The useful bit is that it takes _much_ longer to guess the correct password.

### Does P Equal NP?

The `P` versus `NP` problem is a [major unsolved problem](https://en.wikipedia.org/wiki/P_versus_NP_problem) in computer science. It asks whether every problem whose solution can be quickly _verified_ (is in `NP`) can also be solved quickly (is in `P`).

The question is, "Are all `NP` problems really just `P` problems?"

The answer is, "We don't know, but probably not".

### Why Do We Care?

All problems in `NP` (you know, hard ones like the traveling salesman problem) have been proven to also be solvable in polynomial time if we can find a solution to just one `NP-Complete` problem.

If a _single_ `NP-complete` problem can be solved quickly (in polynomial time) that means that all problems in NP can be solved in polynomial time. That would be a huge deal, particularly because it would break digital security systems that rely on the difficulty of certain `NP` problems.

### The Negative Case

We do not know for sure if `P` equals `NP` because we can't find any polynomial-time solutions to NP-complete problems. Additionally, we have been unable to prove whether `P` does _not_ equal `NP`. We _suspect_ `P` does not equal `NP` because it has been so difficult to prove that `P = NP`.

That said, it's actually more complicated to prove the negative case. To prove the positive case, that `P = NP`, we simply need to solve an NP-complete problem like TSP in polynomial time. In order to _prove_ the negative case, that `P != NP`, we would need to exhaustively prove that there's no _possible way_ to solve TSP in polynomial time. That's a lot trickier.

### NP-Hard

All `NP-complete` problems are [NP-hard](https://en.wikipedia.org/wiki/NP-hardness), but not all `NP-hard` problems are NP-complete. The determining factor between `NP-complete` and `NP-hard` is that _not all_ `NP-hard` problems are `NP`

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/NP%20Hard.png)

Definition:
 
    A problem is `NP-hard` if _every_ problem in `NP` can be reduced into it in polynomial time

Compare this to the slightly different definiton of `NP-complete`:

    A problem is `NP-complete` if it is in `NP` and _every_ other problem in `NP` can be reduced into it in polynomial time.

The difference is that `NP-complete` problems _must_ be in `NP`, or in other words, they must be verifiable in polynomial time. `NP-hard` has no such restriction

### Prime Factorization

Let's solve a commonly misunderstood problem in computer science - **finding the prime factors of a number**. Almost all modern cryptography, including your browser's HTTPS encryption, is based on the fact that **prime factorization** is slow.

For now, let's focus on the speed of factorization, and how it relates to `P` and `NP`.

Finding a number's prime factors is an `NP` algorithm.

   * When given two primes and their product, all we need to do is some simple multiplication to verify correctness. (polynomial time)
   * Given a number, finding its prime factors is a much more difficult problem. Exponential time is the best we know of.

The trouble is that no one has formally proven that there is not a polynomial time algorithm for finding prime factors. So, we're technically unsure if the problem is in `P` or if it's `NP-complete`.
