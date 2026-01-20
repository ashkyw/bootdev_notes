Example of imperative code:

```py
car = create_car()
car.add_gas(10)
car.clean_windows()button {
  color: red;
}

```

Example of functional code:

```py
return clean_windows(add_gas(create_car()))
```

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

The goal of functional programming is to move close and close to a declarative style. 
In CSS they simply declare a button is red:

```css
button {
  color: red;
}
```
But in python in order to do the same we would need to do a few more steps in order to achieve the same thing:

```py
from tkinter import * # first, import the library
master = Tk() # create a window
master.geometry("200x100") # set the window size
button = Button(master, text="Submit", fg="red").pack() # create a button
master.mainloop() # start the event loop
```
Sigma example

```math
avg = Σx/N

```

1. Σ is just the Greek letter Sigma, and it represents "the sum of a collection".
2. x is the collection of numbers we're averaging.
3. N is the number of elements in the collection.
4. avg is equal to the sum of all the numbers in collection "x" divided by the number of elements in collection "x".

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

# Debugging Functional Programming:

It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. Sometimes you have these "elegant" one-liners that are tricky to debug:

```py
def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
```

If the output of get_player_position is incorrect, it's hard to know what's going on. So we need to break it up! Then you can inspect the moved, slowed, and final variables more easily:

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

    "Set n to 7"
    "Define a function named greet"
    "If x > 10, print a greeting to Alice"

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
