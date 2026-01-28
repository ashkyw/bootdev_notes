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


# Debugging Recursion Tip:

When you debug recursive stuff a couple of safe habits:

* Always ask: “What does this function return at every level?”
* Temporarily log both the argument and the return value, e.g.:

```py
    print("ENTER", parent_directory, current_filepath)
    ...
    print("EXIT", directory_list)
```

# FUCK Recursion:

```py
def list_files(parent_directory, current_filepath=""):
    directory_list = []

    for key in parent_directory:
        new_path = f"{current_filepath}/{key}"
        if parent_directory[key] is None:
            directory_list.append(new_path)
        else:
            directory_list.extend(list_files(parent_directory[key], new_path))
            
    return directory_list
```

Further explanation on how the above works.

**1. “Why do I not need a base case? Won’t this run forever?”**

You do have a base case; it’s just not written as a separate `if` at the top.

Your base case is this branch:
```py
if parent_directory[key] is None:
    directory_list.append(new_path)
```
When `parent_directory[key]` is `None`, that means: “this key is a file, not a directory.”

* In that case you *do not recurse*.
* You just add the file path and move on to the next key in the `for` loop.
* Eventually the loop ends, and the function hits `return directory_list`.

So the recursion only happens in this branch:
```py
else:
    directory_list.extend(list_files(parent_directory[key], new_path))
```
And that branch only runs when `parent_directory[key]` is a **dictionary**, i.e., a real subdirectory. Since your input structure eventually bottoms out in `None` values (files), you keep descending until you reach a file, hit the `if`, and *don’t* recurse. That’s your stopping condition.

In tree-recursion, the base case is often “when this node has no children” or “when this value is not a container,” which is exactly your `None` check.

**2. “How can I create the empty list and it not constantly make a new list every call?”**

You do make a new list on every call:
```py
directory_list = []
```
But that’s okay, even necessary.

Think of each call to `list_files` as a worker:

* Each worker gets:
  * A directory (`parent_directory`)
  * The path so far (`current_filepath`)

* It creates its own `directory_list` to collect **only the files inside that directory and its subdirectories**.

    When it’s done, it `returns` *its* list to its caller.

    The caller then does:
```py
directory_list.extend( child_result )
```

So the overall behavior is:

* Top-level call has its own `directory_list`.
* For each subdirectory, it spawns a recursive call.
* Each recursive call builds its own list, returns it.
* The caller merges those child lists into its own with `.extend(...)`.
* Eventually, the top-most caller returns the final, fully merged list.

This doesn’t cause duplication or resets, because:

* Each call has its own `directory_list`.
* Lists don’t need to be shared between calls; they’re combined by `extend` when the recursive call returns.

If you reused the same list across all calls (e.g., as a global), the logic would get harder to reason about and easier to break.

# Dangers of Recursion

Recursion is great because it's simple and elegant (simple != easy). It's often the most straightforward way to solve a problem.

  1. Stack Overflow: Each function call requires a bit of memory. So, if you recurse too deeply, you can run out of ["stack" memory](https://en.wikipedia.org/wiki/Stack-based_memory_allocation) which will crash your program. (This is what the famous website is named after)
  2. If you don't have a solid base case, you can end up in an infinite loop (which will likely lead to a stack overflow).
  3. Recursion (especially in a language like Python) is often slower than a for loop because each function call requires some memory. [Tail call optimization](https://exploringjs.com/es6/ch_tail-calls.html) can help with this, but Python doesn't support it.

Another recursion example

```py
def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word
    words = document.split(maxsplit=1)
    if len(words) < 1:
        return longest_word
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) < 2:
        return longest_word
    return find_longest_word(words[1], longest_word)

```


