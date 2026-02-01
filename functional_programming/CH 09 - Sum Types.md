# [Sum Types](https://en.wikipedia.org/wiki/Tagged_union)

A "sum" type is the opposite of a "product" type. This Python object is an example of a *product* type:
```py
man.studies_finance = True
man.has_trust_fund = False
```
The total number of combinations a man can have is 4, the product of 2 * 2:

| studies_finance | has_trust_fund |
|:---------------:|:--------------:|
| True            | True           |
| True 	          | False          |
| False           | True           |
| False           | False          |

If we add a third attribute, perhaps a has_blue_eyes boolean, the total number of possibilities multiplies again, to 8!
studies_finance 	has_trust_fund 	has_blue_eyes
True 	True 	True
True 	True 	False
True 	False 	True
True 	False 	False
False 	True 	True
False 	True 	False
False 	False 	True
False 	False 	False

But let's pretend that we live in a world where there are really only three types of people that our program cares about:

    Dateable
    Undateable
    Maybe dateable

We can reduce the number of cases our code needs to handle by using a (admittedly fake Pythonic) sum type with only 3 possible types:

class Person:
    def __init__(self, name):
        self.name = name

class Dateable(Person):
    pass

class MaybeDateable(Person):
    pass

class Undateable(Person):
    pass

Then we can use the isinstance built-in function to check if a Person is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.

def respond_to_text(guy_at_bar):
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid person type")

Sum Types

As opposed to product types, which can have many (often infinite) combinations, sum types have a fixed number of possible values. To be clear: Python doesn't really support sum types. We have to use a workaround and invent our own little system and enforce it ourselves.
