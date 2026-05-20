
# Pure Functions

If you take nothing else away from this course, *please* take this: [Pure functions](https://en.wikipedia.org/wiki/Pure_function) **are fantastic.** They have two properties:

* They always return the same value given the same arguments.
* Running them causes no side effects

Pure functions have a lot of benefits. Whenever possible, good developers try to use pure functions instead of impure functions. Remember, pure functions:

* Return the same result if given the same arguments. They are [deterministic](https://en.wikipedia.org/wiki/Deterministic_system).
* Do not change the external state of the program. For example, they do not change any variables outside of their scope.
* Do not perform any [I/O operations](https://en.wikipedia.org/wiki/Input/output) (like reading from disk, accessing the internet, or writing to the console).

These properties result in pure functions being easier to test, debug, and think about.

Refer to the following examples and answer the questions.

In short: **pure functions don't do anything with anything that exists outside of their scope.**

# Example of a Pure Function
```py
def find_max(nums):
    max_val = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```

Example of an Impure Function
```py
# instead of returning a value
# this function modifies a global variable
global_max = float("-inf")

def find_max(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```

Another example of a Pure Function
```py
def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
        "docx": ["pdf", "txt", "md"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx", "pdf", "md"],
        "pptx": ["ppt", "pdf"],
        "ppt": ["pptx", "pdf"],
        "md": ["docx", "pdf", "txt"],
    }

    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None
```
# Reference vs. Value

When you pass a value into a function as an argument, one of two things can happen:

* It's passed by **reference**: The function has access to the original value and can change it.
* It's passed by **value**: The function only has access to a copy. Changes to the copy within the function don't affect the original.

*There is a bit more nuance, but this explanation mostly works.*

These types are passed by **reference**:

* Lists
* Dictionaries
* Sets

These types are passed by **value**:

* Integers
* Floats
* Strings
* Booleans
* Tuples

Most collection types are passed by reference (except for tuples) and most primitive types are passed by value.

# Example of Pass by Reference (Mutable)

```py
def modify_list(inner_lst):
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]
```

# Example of Pass by Value (Immutable)

```py
def attempt_to_modify(inner_num):
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num = 1
attempt_to_modify(outer_num)
# outer_num = 1
```
# Pass by Reference Impurity

Because certain types in Python are passed by reference, we can mutate values that we didn't intend to. This is a form of function impurity.

Remember, a pure function should have *no side effects.* It shouldn't modify anything outside of its scope, *including its inputs.* It should return new copies of inputs instead of changing them.

# Pure Function
```py
def remove_format(default_formats, old_format):
    new_formats = default_formats.copy()
    new_formats[old_format] = False
    return new_formats
```
# Impure Function
```py
def remove_format(default_formats, old_format):
    default_formats[old_format] = False
    return default_formats
```

# Why Do We Care?

One of the biggest differences between good and great developers is how often they incorporate pure functions into their code. Pure functions are easier to read, easier to reason about, easier to test, and easier to combine. Even if you're working in an imperative language like Python, you can (and should) write pure functions whenever reasonable.

There's nothing worse than trying to debug a program where the order of function calls needs to be juuuuust right because they all read and modify the same global variable.

# Input and Output

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Cartoon.png)The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world". "Outside world" just means anything that's not stored in our application's memory (like variables).

# Examples of I/O

* Reading from or writing to a file on the hard drive
* Accessing the internet
* Reading from or writing to a database
* Even simply printing to the console is considered i/o!

All i/o is a form of "side effect".

# Should I I/O?

A program that doesn't do *any* i/o is pretty useless. What's the point of computing something if you can't see the results?

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/spongebob.png)

In functional programming, i/o is viewed as *dirty* but *necessary*. We know we can't *eliminate* i/o from our code, so we just *contain* it as much as possible. There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure.

For example, a Python program might:

1. Read a file from the hard drive as the program starts
2. Run a bunch of pure functions to analyze the data
3. Write the results of the analysis to a file on the hard drive at the end

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/functional_i-o_tree.png)

# No-Op

A [no-op](https://en.wikipedia.org/wiki/NOP_(code)) is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. If it doesn't return anything, the only reason for it to exist is to perform a side effect.

# Example No-Op

This function performs a useless computation because it doesn't return anything or perform a side effect. It's a no-op.
```pydef restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )

def square(x):
    x * x
```
# Example Side Effect

This function performs a side effect. It changes the value of the y variable that is outside of its scope. It's impure.
```py
y = 5
def add_to_y(x):
    global y
    y += x

add_to_y(3)
# y = 8
```
> [!Note]
> The `global` keyword just tells Python to allow modification of the outer-scoped `y` variable.

# print()

Even the `print` function (technically) has an impure side effect! It doesn't return anything, but it does print text to the console, which is a form of I/O.

# Memoization

At its core, [memoization](https://en.wikipedia.org/wiki/Memoization) is just [caching](https://en.wikipedia.org/wiki/Cache_(computing)) (storing a copy of) the result of a computation so that we don't have to compute it again in the future.

For example, take this simple function:
```py
def add(x, y):
    return x + y
```
A call to `add(5, 7)` will *always* evaluate to `12`. So, if you think about it, once we know that `add(5, 7)` can be replaced with `12`, we can just store the value `12` somewhere in memory so that we don't have to do the addition operation again in the future. Then, if we need to `add(5, 7)` again, we can just look up the value `12` instead of doing a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

> [!Note]
> It's pronounced "memOization", not "memORization". This confused me for quite a while in college, I thought my professor just didn't speak goodly...

# Referential Transparency

Pure functions are always [referentially transparent](https://www.baeldung.com/cs/referential-transparency#referential-transparency).

"Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. *Referentially transparent functions can be safely memoized.* For example `add(2, 3)` can be smartly replaced by the value `5`.

The great thing about pure functions is that they can always be safely memoized. Impure functions can't be because they might do something in addition to returning a static value, or they might return different values given the same arguments.

# Should I Always Memoize?

No! Memoization is a *tradeoff* between memory and speed. If your function is fast to execute, it's probably not worth memoizing, because the amount of RAM (memory) your program will need to store the results will go way up.

It's also a bunch of extra code to write, so you should only do it if you have a good reason to.
