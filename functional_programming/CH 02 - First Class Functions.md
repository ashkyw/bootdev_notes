# Functions as values:

In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:

```py
def add(x, y):
    return x + y

# assign the function to a new variable
# called "addition". It behaves the same
# as the original "add" function
addition = add
print(addition(2, 5))
# 7
```

# Lambda functions:
Anonymous functions have no name, and in Python, they're called [Lambda Functions](https://docs.python.org/3/reference/expressions.html#lambda)

Here's a lambda function that takes a single argument `x` and returns the result of `x + 1`:

```py
lambda x: x + 1
```

Notice that the [expression](https://docs.python.org/3/reference/expressions.html#expressions) `x + 1` is returned automatically, no need for a `return` statement. Compare that to how you'd normally write a function:

```py
def add_one(x):
    return x + 1
```

Because functions are just values, we can assign the function to a variable named `add_one`:

```py
add_one = lambda x: x + 1
print(add_one(2))
# 3
```

Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations. Here's an example that uses a lambda to get a value from a dictionary:

```py
get_age = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29
```

Example of lambda function:

```py
def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")
```

# First Class and Higher Order Functions

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

* First-class function: A function that is treated like any other value
* Higher-order function: A function that accepts another function as an argument or returns a function

Python supports first-class and higher-order functions.

# First-Class Example
```py
def square(x):
    return x * x

# Assign function to a variable
f = square

print(f(5))
# 25
```
# Higher-Order Example
```py
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```

# Map

"Map", "filter", and "reduce" are three commonly used [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function) in functional programming.

In Python, the built-in [map](https://docs.python.org/3/library/functions.html#map) function takes a function and an [iterable](https://docs.python.org/3/glossary.html#term-iterable) (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/map.png)

With map, we can operate on lists without using loops and nasty stateful variables. For example, given this code:
```py
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = []
for num in nums:
    num_squared = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]
```
We could use map instead, like this:
```py
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```
> [!Note]
> `map()` returns a "map object", so the [`list()` type constructor](https://docs.python.org/3/library/stdtypes.html#list) is needed to convert it back into a standard list.

Another example of `map()`:
```py
def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))

def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
```
# Filter

The built-in [filter](https://docs.python.org/3/library/functions.html#filter) function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned `True`.

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/filter.png)

In Python:
```py

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```
Example of overly complex, shitty one-liners in Python:
```py
def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )
```
# Reduce

The built-in [functools.reduce()](https://docs.python.org/3/library/functools.html#functools.reduce) function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes.

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/reduce.png)

```py
# import functools from the standard library
import functools

def add(sum_so_far, x):
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers = [1, 2, 3, 4]
sum = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10
```

Notice that we are passing the function `add` without the `()`.

It means that `reduce` will take care of the execution and pass the parameters for you.

Think of passing `add` like handing someone a recipe (the instructions), instead
of the finished dish (the result of the execution).

Another example of `functools.reduce()`:
```py
import functools

def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence

def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."
```

# Map, Filter, and Reduce Review

Higher-order functions like `map`, `filter`, and `reduce`, allow us to avoid stateful iteration and mutations of variables.

Take a look at this imperative code that calculates the factorial of a number:
```py
def factorial(n):
    # a procedure that continuously multiplies
    # the current result by the next number
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
Here's the same factorial function using `reduce`:
```py
import functools

def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))
```
In the functional example, we're just combining functions to get the result we want. There's no need to reassign variables or keep track of the program's state in a loop.

A loop is inherently stateful. Depending on which iteration you're on, the i variable has a different value.

# Zip

The [zip](https://docs.python.org/3/library/functions.html#zip) function takes two iterables (in this case lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.
```py
a = [1, 2, 3]
b = [4, 5, 6]

c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```
One more one-liner example of functional programming combining a lot of things:

```py
def restore_documents(originals, backups):
    return set(
        filter(
            lambda doc: not doc.isdigit(),
            map(lambda doc: doc.upper(), originals + backups),
        )
    )
```
