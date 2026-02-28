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
