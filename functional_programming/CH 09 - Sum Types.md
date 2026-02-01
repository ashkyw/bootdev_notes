# [Sum Types](https://en.wikipedia.org/wiki/Tagged_union)

A "sum" type is the opposite of a "product" type. This Python object is an example of a *product* type:
```py
man.studies_finance = True
man.has_trust_fund = False
```
The total number of combinations a `man` can have is `4`, the *product* of `2 * 2`:

| studies_finance | has_trust_fund |
|:---------------:|:--------------:|
| True            | True           |
| True 	          | False          |
| False           | True           |
| False           | False          |

If we add a third attribute, perhaps a `has_blue_eyes` boolean, the total number of possibilities multiplies again, to `8`!

|studies_finance  |	has_trust_fund  |  has_blue_eyes  |
|:---------------:|:---------------:|:---------------:|
|    True 	      |     True 	    |       True      |
|    True 	      |     True 	    |       False     |     
|    True 	      |     False 	    |       True      |
|    True 	      |     False 	    |       False     |
|    False 	      |     True 	    |       True      |
|    False 	      |     True 	    |       False     |
|    False 	      |     False 	    |       True      |
|    False 	      |     False 	    |       False     |

But let's pretend that we live in a world where there are *really* only three types of people that our program cares about:

1. Dateable
2. Undateable
3. Maybe dateable

We can *reduce* the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible *types*:
```py
class Person:
    def __init__(self, name):
        self.name = name

class Dateable(Person):
    pass

class MaybeDateable(Person):
    pass

class Undateable(Person):
    pass
```
Then we can use the isinstance built-in function to check if a `Person` is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.
```py
def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid person type")
```
# Sum Types

As opposed to product types, which can have many (often infinite) combinations, sum types have a *fixed* number of possible values. To be clear: **Python doesn't really support sum types**. We have to use a workaround and invent our own little system and enforce it ourselves.

# Enums

Doing the admittedly weird `class` and `isinstance()` thing works, but it turns out, there's a better way in some cases. If you're trying to represent a fixed set of values (but not store additional data within them) [enums](https://docs.python.org/3/library/enum.html) are the way to go.

[Enum Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/enums_python-1920x1080.mp4)

Let's say we have a `Color` variable that we want to restrict to only three possible values:

* RED
* GREEN
* BLUE

We could use a plain-old `string` to represent these values, but that's annoying because we have to remember all the "valid" values and defensively check for invalid ones all over our codebase. Instead, we can use an `Enum`:
```py
from enum import Enum

Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception
```
There is also a class-based syntax for creating enums:
```py
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL) # this raises an exception
```
Now `Color` is a sum type! *At least, as close as we can get in Python*.

There are a few benefits:

1. A "Color" can only be `RED`, `GREEN`, or `BLUE`. If you try to use `Color.TEAL`, Python raises an exception.
2. There is a central place to see the "valid" values for a `Color`.
3. Each "Color" has a "name" (e.g. `Color.RED`) and a "value" (e.g. `1`). The value is an integer and is used under the hood instead of the name. Integers take up less memory than strings, which helps with performance.
