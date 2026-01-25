# Functional Programming:

Functional Programming is a Style or Paradigm where we compse functions instead of mutating state (updating the values of variables)
Functional programming is about declaring **what** you want to happen, rather than *how* you want it to happen.

Functional example:
```py
return clean_windows(add_gas(create_car()))
```

Imperative programming (or procedural) declares both the **what** and the *how*.

Imperative Example:
```py
car = create_car()
car.add_gas(10)
car.clean_windows()
```
In functional programming we never change the value of the `car` variable, we just compose functions that return new values with the `clean_windows` function returning the final result.

# Immutability

Functional programming strives to make our data immutable. Immutable data is easier to think about & work with. When several functions have access to the same variable & you're debugging a problem with a mutable variable you have to consider the possibilty that *any* functions that touched it could have changed the value. Where when something is immutable you know it hasn't been changed after it's creation. This makes code much easier to maintain and debug.

Tuples are immutable. Example of creating a new tuple and adding that to existing tuple:

```py
ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)
```

Another example of tuples:

```py
def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents

```
# Declarative Styling

The goal of functional programming is to move closer and closer to a declarative style. 
In CSS they simply declare a button is red:

```css
button {
  color: red;
}
```
# Imperative Styling

But in python in order to do the same we would need to do a few more steps in order to achieve the same thing:

```py
from tkinter import * # first, import the library
master = Tk() # create a window
master.geometry("200x100") # set the window size
button = Button(master, text="Submit", fg="red").pack() # create a button
master.mainloop() # start the event loop
```

# Da Maff

Functional programming is popular among people with a strong math background since equations are declarative, **not** procedural.

```math
avg = Σx/N
```

1. `Σ` is just the Greek letter Sigma, and it represents "the sum of a collection".
2. `x` is the collection of numbers we're averaging.
3. `N` is the number of elements in the collection.
4. `avg` is equal to the sum of all the numbers in collection "x" divided by the number of elements in collection "x".

So, the equation really just says that avg is the average of all the numbers in collection "x". This math equation is a declarative way of writing "calculate the average of a list of numbers". Here's some imperative Python code that does the same thing:

```py
def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

However, with functional programming, we would write code that's a bit more declarative:

```py
def get_average(nums):
    return sum(nums) / len(nums)
```

Example of good, one line functional programming:

```py
def get_median_font_size(font_sizes):
    if len(font_sizes) == 0:
        return None
    return sorted(font_sizes)[(len(font_sizes) - 1) // 2]
```

# Classes vs. Functions

Functions are *not* inferior to `classes`, they are just different.

# When to use classes or functions

Good rule of thumb:

> If you're unsure, default to functions. Classes are good when something will be long lived,     stateful, & would be easier to model with shared behavior & data structure via inheritance.
Often these are the case with video games, simulations & GUIs.

Key differences:

> **Classes** encourage you to think about the world as a hierarchical collection of `objects`.
`Objects` bundle behavior, data, & state together in a way that draws boundaries between instances of things, like Chess pieces on a board.

> **Functions** encourage you to think about the world as a series of data transformations.       > They take data as input & return a transformed output.

# Debugging Functional Programming:

It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. Sometimes you have these "elegant" one-liners that are tricky to debug:

```py
def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
```

If the output of `get_player_position` is incorrect, it's hard to know what's going on. So we need to break it up! Then you can inspect the moved, slowed, and final variables more easily:

```py
def get_player_position(position, velocity, friction, gravity):
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final
```
Once you've run it, found the issue, solved it, then you can remove print statements.

Functional programming and object-oriented programming are styles for writing code. One isn't inherently superior to the other, but to be a well-rounded developer you should understand both well and use ideas from each when appropriate.

You'll encounter developers who love functional programming and others who love object-oriented programming. However, contrary to popular opinion, FP and OOP are not always at odds with one another. They aren't opposites. Of the four pillars of OOP, inheritance is the only one that doesn't fit with functional programming.

![Alt Text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/FP%20OOP%20Ven.png)

Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation, polymorphism and abstraction are still used all the time in functional programming.

When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) the best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.

# Statements vs. Expressions

Studying functional programming is really about returning to the most basic aspects of programming and looking at them in a new way. Statements and expressions are a great example of that.

# Statements

"Statements" are actions to be carried out. For example:

* "Set n to 7"
* "Define a function named greet"
* "If x > 10, print a greeting to Alice"

In Python, such statements look like this:
```py
n = 7  # Variable assignment statement

def greet(name):  # Function definition statement
    return f"Hello, {name}!"

if x > 10:  # `if` statement
    print(greet("Alice"))

for i in range(n):  # `for` loop statement
    print(i)
```
Every complete instruction is a statement.

# Expressions

Expressions are a subset of statements that produce values. Evaluating an expression results in a value that can be used in whatever way is needed. It can be assigned to a variable, returned from a function, etc.

```py
result = 2 + 2  # Arithmetic expression
length = len("hello")  # Function call expression
total_cost = len(items) * cost  # Multiple expressions combined into one
```

One thing that may surprise you is that, in most languages (including Python), every function call is an expression. When you call a function, it returns a value – whether or not you realize it or do anything with that value. Even if a Python function doesn't have a `return` statement, it still implicitly returns `None`. You can test this by assigning a `print` call to a variable:

```py
x = print("hello")  # hello
print(x)            # None
```

Sure enough: `print` – the first function that we all learn – technically returns a value.
Expressions Over Statements

Because expressions always produce values, they're reusable and declarative. You can compose expressions and nest them within each other – but you can't always do that with other kinds of statements. Functional programming encourages the use of expressions over statements where possible, because expressions tend to minimize side effects, and make the code easier to reason about. For example, a function that returns a sum is an expression:

```py
total = sum([1, 2, 3, 4])
```

We can get the same result with a loop, but that involves a series of statements:

```py
total = 0
for n in [1, 2, 3, 4]:
    total += n
```

Again, it's simple to combine expressions:

```py
print(sum([1, 2, 3, 4]) * 2)  # 20
```

But we can't really do the same thing with our series of statements:

```py
# This doesn't work!
print((
total = 0
for n in [1, 2, 3, 4]:
    total += n
) * 4)
```

Expressions tend to be concise and logically pure. Some languages that are designed for functional programming, such as Haskell, actually treat everything as an expression. In these languages, even control flow constructs like if and case are expressions that return values.

# Ternary Expressions

[Ternaries](https://book.pythontips.com/en/latest/ternary_operators.html) are a great way to reduce a series of statements, like an `if/else` block, to a single expression.

When you first learning how to use conditional logic in Python, it typically looks like this:

```py
result = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1
```

This sets `result` to a dummy value `0` (`None` would also work), then overwrites it with its "real" value based on the condition.

A ternary lets us do all that in one expression:

```py
result = number / 2 if number % 2 == 0 else (number * 3) + 1
```

Note that we also avoided mutating the `result` variable. Ternary expressions are good for maintaining immutability.

The syntax for a ternary in Python is:
```py
value_a if condition else value_b
```
This qualifies as an expression because it's a single statement that evaluates to a value – one of two values, depending on the condition.

# When to Use Ternaries

Ternary expressions are cool, but don't overdo it. If you're dealing with complex conditional logic, it's often easier to work with full `if/else` blocks than to try to nest ternaries inside each other.

```py
msg = (
    "Access granted"
    if (
        user.is_authenticated
        and (user.role == "admin" or (user.role == "editor" and not user.suspended))
    )
    else ("Access limited" if user.is_authenticated else "Access denied")
)
```

Another example of ternary:

```py
def choose_parser(file_extension):
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
```

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
# outer_lst = [1, 2, 3, 4]````
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
```py
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

