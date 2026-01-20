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

Debugging Functional Programming:

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

!Alt Text

Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation, polymorphism and abstraction are still used all the time in functional programming.

When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) the best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.
