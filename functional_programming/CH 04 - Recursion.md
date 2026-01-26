# Recursion

[Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
is notoriously hard to understand. Ultimately, it's just a function that calls itself.

[Recursion Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Recursion-explained-1920x1080.mp4)

```py
def countdown(n):
  print(n)
  countdown(n-1)
```

Would `print` `n` then calls itself and `print`s `n`-1
```py
countdown(5)
#5
countdown(4)
#4
```
This iteration will run forever.
Recursion requires a base case to prevent infinite loops.

```py
def countdown(n)
  if n <=0:
    print("Blastoff!")
  print(n)
  countdown(n-1)
```
The conditional statement would stop the infinite loop as soon as n hits 0

# Example of Recursion

If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:
```py
def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
```
Don't break your brain on the example above! Let's break it down step by step:

**1. Solve a Small Problem**

Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:

```py
return nums[0] + sum_nums(nums[1:])
```

**2. Recurse**

So, what actually happens when we call `sum_nums(nums[1:])`? Well, we're just calling `sum_nums` with a smaller list! In the first call, the `nums` input was `[1, 2, 3, 4, 5]`, but in the next call it's just `[2, 3, 4, 5]`. We just keep calling `sum_nums` with smaller and smaller lists.

**3. The Base Case**

So what happens when we get to the "end"? `sum_nums(nums[1:])` is called, but `nums[1:]` is an empty list because we ran out of numbers. We need to write a base case to stop the madness.

```py
if len(nums) == 0:
    return 0
```

The "base case" of a recursive function is the part of the function that does *not* call itself.

```py
def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    new_dict = zipmap(keys[1:], values[1:])
    new_dict[keys[0]] = values[0]
    return new_dict
```
Think of the recursion like a stack of plates:

1. Each call to `zipmap(keys, values)` is one plate on the stack.
2. The **base case** (`len(keys) == 0 or len(values) == 0`) is the *bottom* plate.
   That’s where the empty dictionary `{}` is first created.
3. Every other call above it waits for the call below to finish, then adds one key/value pair.

Concretely, with:
```py
keys   = ["A", "B", "C"]
values = [1,   2,   3]
```
The calls look like this, from top to bottom:

  * Call 1: `zipmap(["A", "B", "C"], [1, 2, 3])`
  * Call 2: `zipmap(["B", "C"], [2, 3])`
  * Call 3: `zipmap(["C"], [3])`
  * Call 4: `zipmap([], [])` → base case → returns `{}`

Now we unwind:

  * Call 4 returns `{}` to Call 3.
  * Call 3 takes that `{}`, adds `"C": 3`, returns `{"C": 3}`.
  * Call 2 takes `{"C": 3}`, adds `"B": 2`, returns `{"C": 3, "B": 2}`.
  * Call 1 takes `{"C": 3, "B": 2}`, adds `"A": 1`, returns `{"C": 3, "B": 2, "A": 1}`.

So:

* The dict is **created once** at the very bottom (`{}`).
* Each higher call uses the *returned dict* (via your `new_dict` variable), mutates it, and returns it again.
* By the time the *first call* finishes, you have a fully built dictionary you can use like any normal dict.

Key mental model:

* Recursion builds the result **bottom‑up**, returning a partial result each time.
* Your top‑level call just gets the final result of all those smaller steps.

1. Conditionals vs. base cases
* With a normal `if`, you think: “If this situation ever happens, do X.”
* With recursion, the base case is more like: *“This is the definition of the answer for the smallest possible input.”*
* It’s not about *when* it happens in time, it’s about *what the answer* is for that minimal case.

2. “How we start” vs. “how we build”
* The base case defines the **starting value** of the computation (`0`, `{}`, `""`, etc.).
* The recursive step defines **how to go from a smaller solved problem to a bigger one**.

So the mental recipe:
* “If input is tiny (empty list, empty string, no nodes…) → here is the final answer for that: base case.”
* “Otherwise → assume the smaller version is already solved, then add my one piece.”

# Recursion Review

Recursion is so *dang useful* with tree-like structures because we don't always know how deep they're nested. Stop and think about how you would write nested loops to traverse a tree of arbitrary depth... it's not easy, is it?

```py
for item in tree:
    for nested_item in item:
        for nested_nested_item in nested_item:
            for nested_nested_nested_item in nested_nested_item:
                # ... WHEN DOES IT END???
```
I most often use recursion on tree-like problems (file systems, nested dictionaries, etc). If I'm just iterating over a one-dimensional list then a loop (*gasp...*) is typically simpler, even if it's not as "pure" in the academic sense.

*Remember: The rules of functional programming are just philosophies to help you write better code, but it's not always the right tool for the job.* The same goes for any programming paradigm.
