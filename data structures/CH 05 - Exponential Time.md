# Polynomial vs. Exponential

Broadly speaking, algorithms can be classified into two categories:

* "Polynomial time"
* "Exponential time"

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/exponential%20time.png)

Technically `O(n!)` is "factorial" time, but let's lump them together for simplicity

An algorithm runs in "Polynomial time" if its runtime does not grow faster than `n^k`, where `k` is any constant (e.g. `n^2`, `n^3`, etc) and n is the size of the input. Polynomial-time algorithms can be useful if they're not too slow.

In comparison, exponential-time algorithms are almost always too slow to be practical. (However, sometimes you're trying to force someone to be slow, like in the case of cryptography and security). Even when `n` is as low as `20`, `2^n` is already over a million!

| `n` |	`n^2` |	`2^n` |
|:-:|:---:|:---:|
| 2 |	 4  | 	4    |
| 3 |	 9  |	 8     |
| 4 |	 16 |	 16    |
| 5 |	 25 |  32    | 
| 6 |	 36 |	64     |
| 7 |	 49 |	128    |
| 8 |  64 | 256    |
| 9 |	 81 | 512    |
| 10|  100| 1024   |
| 11|  121| 2048   |
| 12|  144|	4096   |
| 13|  169| 8192   |
| 14|  196|	16384  |
| 15|  225| 	32768|
| 16|  256| 	65536|
| 17|  289|  131072|
| 18|  324|  262144|
| 19|  361|  524288|
| 20|  400| 1048576|

### Polynomial Time = P

Back in the 1970s, some computer scientists wanted to come up with a good, descriptive name for the set of polynomial time algorithms. After much deliberation, they settled on the letter `P` [(naming things is hard)](https://xkcd.com/910/).

The hand-wavy takeaway is that:

* Problems that fall into class `P` are practical to solve on computers.
* Problems that don't fall into `P` are hard, slow, and impractical.

### Reduction to P

Let's take an exponential time algorithm and fix it up so it can run in polynomial time!

The [Fibonacci sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) is a sequence of numbers where each number is the sum of the two numbers before it. Like this:

```math
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

We want a function that, given an index in the sequence, returns the Fibonacci number at that index. For example:

* `fib(0)` -> 0
* `fib(1)` -> 1
* `fib(2)` -> 1
* `fib(3)`t -> 2
* `fib(4)` -> 3
* `fib(5)` -> 5
* `fib(6)` -> 8
* `fib(7)` -> 13

Here are the implementation details to do it in polynomial time:

1. The input `n` represents the index of the desired Fibonacci number.
2. If `n` is less than or equal to 1, then return `n`.
3. Initialize three variables: `grandparent = 0`, `parent = 1`, and a placeholder `current` to store the new Fibonacci number at each step.
4. Write a loop that iterates `n - 1` times. (For example, if `n = 2`, one iteration occurs.)
5. Inside the loop:
    1. Set `current = parent + grandparent`
    2. Adjust the ancestor values (`parent` and `grandparent`) to maintain the sequence.
    Once the loop completes, return current.

Fibonacci in python:
```py
def fib(n):
    if n <= 1:
        return n
    grandparent = 0
    parent = 1
    for i in range(n-1):
        current = parent + grandparent
        grandparent = parent
        parent = current
        
    return current
```

### Order K^N – Exponential

`O(K^N)` – where `K` represents a constant branching factor, e.g. `3^N` – is the first Big O class that we've dealt with that falls into the scary exponential category of algorithms.

Algorithms that grow at an exponential rate become impossible to compute after so little scale-up that they're usually almost worthless in practicality.

### Big O Categories Review

|Big-O|Name| Description|
|:-:|:-:|:-:|
|O(1)| 	constant| 	**Best** The algorithm always takes the same amount of time, regardless of how much data there is. Example: Looking up an item in a list by index|
|O(log(n))| 	logarithmic |	**Great** Algorithms that remove a percentage of the total steps with each iteration. Very fast, even with large amounts of data. Example: Binary search|
|O(n) |	linear| 	**Good** 100 items, 100 units of work. 200 items, 200 units of work. This is usually the case for a single, non-nested loop. Example: unsorted array search.|
|O(n*log(n)) 	|"linearithmic" |	**Okay** This is slightly worse than linear, but not too bad. Example: mergesort and other "fast" sorting algorithms.|
|O(n^2) |	quadratic |	**Slow** The amount of work is the square of the input size. 10 inputs, 100 units of work. 100 Inputs, 10,000 units of work. Example: A nested for loop to find all the ordered pairs in a list.|
|O(n^3) |	cubic |	**Slower** If you have 100 items, this does 100^3 = 1,000,000 units of work. Example: A triple nested for loop to find all the ordered triples in a list.|
|O(2^n) |	exponential |	**Horrible** We want to avoid this kind of algorithm at all costs. Adding one to the input doubles the amount of steps. Example: Brute-force guessing results of a sequence of n coin flips.|
|O(n!) |	factorial |	**Even More Horrible** The algorithm becomes so slow so fast, that it is practically unusable. Example: Generating all the permutations of a list|
