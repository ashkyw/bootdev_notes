Basic example of using polymorphism to check if boxes are overlapping based on cartesian coords.
```py
class Rectangle:
    def overlaps(self, rect):
        if (
            self.get_left_x() <= rect.get_right_x() and 
            self.get_right_x() >= rect.get_left_x() and 
            self.get_top_y() >= rect.get_bottom_y() and 
            self.get_bottom_y() <= rect.get_top_y()
            ):
                return True
        return False

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
```
Explanation of `class` code execution order:

There are two levels of “order” to think about:

1. Module level (top to bottom)

Python does run the file itself top to bottom:

    First it defines Unit
    Then it defines Dragon
    Then it defines Rectangle
    Then any code that runs at the bottom (like tests)

But “define a `class`” means: Python reads the whole `class Rectangle`: block, executes its body to build the `class` object, and only then binds the name Rectangle to that finished `class`.

Inside that `class` body, order still matters, but in a different way.

2. Inside the `class` body

When Python sees:
```py
class Rectangle:
    def overlaps(self, rect):
        ...
    def __init__(self, x1, y1, x2, y2):
        ...
```
it:

    Executes the body top to bottom.
    Each `def` just creates a function object and assigns it as an attribute on the `class` being built.

So after the `class` statement is done, you end up with a Rectangle that has both:

    a `Rectangle.overlaps` method
    a `Rectangle.__init__` method

The order of those two defs doesn’t matter for calling them later. When you write:
```py
r = Rectangle(1, 2, 3, 4)
```
Python looks up `Rectangle.__init__` on the finished `class`; it doesn’t care that overlaps was listed first.

The only time order inside the `class` would really matter is if you tried to do something like:
```py
class Rectangle:
    print(__init__)  # This would fail if __init__ isn't defined yet
    def __init__(...):
        ...
```
But normal methods calling each other or being called from outside are fine, regardless of their order in the `class`.
How this ties back to your concern

    When you write self.__hit_box = Rectangle(...) in Dragon.__init__, that happens only when a Dragon object is created at runtime, not when Python is first reading the file.
    By the time any Dragon is instantiated, the whole file has been executed top-to-bottom, so the Rectangle class (with both __init__ and overlaps) is already fully defined.

So:

    Yes, the file runs top to bottom.
    But within class Rectangle, the order of def __init__ vs def overlaps doesn’t affect your ability to call them later. They both exist on the class once the class statement finishes.

Example of polymorphism with double inheritance:
```py
class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        half_height = height / 2
        half_width = width / 2
        self.__hit_box = Rectangle(
            pos_x - half_width,
            pos_y - half_height,
            pos_x + half_width,
            pos_y + half_height,
        )

    def in_area(self, x1, y1, x2, y2):
        r1 = Rectangle(x1, y1, x2, y2)
        return r1.overlaps(self.__hit_box)

class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2
```
Explanation of how to utilize classes in bigger projects with multiple files:

In real projects, it’s very common to:

    Put related classes/functions into their own module files.
    Then import them into the files that use them.

For example, you might have:
```py
# rectangle.py
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        ...
    def overlaps(self, rect):
        ...

# units.py
from rectangle import Rectangle

class Unit:
    ...
class Dragon(Unit):
    ...

# main.py
from units import Dragon

def main():
    d = Dragon("Smaug", 0, 0, 10, 10, 5)
    ...
```
Same import mechanics as with functions—modules are just files, and you import names (`classes`, `functions`, `variables`) from them.

Typical guidelines:

    One module per “concept” or tight group of concepts.
        e.g. geometry.py for Rectangle, Circle, etc.
        units.py for Unit, Dragon, Archer, etc.
    Keep your main.py fairly small—often just wiring things together, parsing args, running the game/app.

As your projects grow past “single small script”, splitting code into modules like this is the normal next step.

hit_by_fire example
```py
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health

```
What Is a Function Signature?

A function signature (or method signature) includes the name, inputs, and outputs of a function or method. For example, hit_by_fire in the Human and Archer classes have identical signatures.

```py
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
```
Both methods have the same name, take no additional inputs, and return integers. If any of those things were different, they would have different function signatures. Here are methods with different signatures:
```py
class Human:
    def hit_by_fire(self):
        self.health -= 5
        return self.health

class Archer:
    def hit_by_fire(self, dmg):
        self.health -= dmg
        return self.health

<class point default>

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```
class point with __add__
```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)
```
CH:6 - 9 Solution
```py
class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        raise Exception("cannot craft")
```
Dunder methods to overload other operators
```py
Operation 	        Operator 	Method
Addition     	        + 	    __add__
Subtraction 	        - 	    __sub__
Multiplication 	        * 	    __mul__
Power 	                ** 	    __pow__
Division 	            / 	    __truediv__
Floor Division 	        // 	    __floordiv__
Remainder (modulo) 	    % 	    __mod__
Bitwise Left Shift 	    << 	    __lshift__
Bitwise Right Shift     >> 	    __rshift__
Bitwise AND 	        & 	    __and__
Bitwise OR         	    | 	    __or__
Bitwise XOR 	        ^ 	    __xor__
Bitwise NOT 	        ~ 	    __invert__
```
# print example
```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
print(p1)
# prints "<Point object at 0xa0acf8>"
```
That's not super useful! We probably want to see the fields!

Let's teach our Point class to print itself. The `__str__` method (short for "string") lets us do just that. It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.
```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"

The __repr__ method works similarly: the difference is that it's intended for use in debugging by developers, rather than in printing strings to end users.

<Overloading multiple cards operators>

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            other.rank_index == self.rank_index and other.suit_index == self.suit_index
        )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    def __str__(self):
        return f"{self.rank} of {self.suit}"

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
```
extended overloading with other classes inheritance
    
```py
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and self.suit_index == other.suit_index
        )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Round:
    def resolve_round(self):
        raise NotImplementedError("Subclasses must implement resolve_round()")

class HighCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self):
        if self.card1 == self.card2:
            return 0
        if self.card1 > self.card2:
            return 1
        if self.card1 < self.card2:
            return 2

class LowCardRound(Round):
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def resolve_round(self):
        if self.card1 == self.card2:
            return 0
        if self.card1 < self.card2:
            return 1
        if self.card1 > self.card2:
            return 2
```
