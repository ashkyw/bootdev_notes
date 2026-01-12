Basic example of using polymorphism to check if boxes are overlapping based on cartesian coords.

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

Explanation of Class code execution order:

There are two levels of “order” to think about:
1. Module level (top to bottom)

Python does run the file itself top to bottom:

    First it defines Unit
    Then it defines Dragon
    Then it defines Rectangle
    Then any code that runs at the bottom (like tests)

But “define a class” means: Python reads the whole class Rectangle: block, executes its body to build the class object, and only then binds the name Rectangle to that finished class.

Inside that class body, order still matters, but in a different way.
2. Inside the class body

When Python sees:

class Rectangle:
    def overlaps(self, rect):
        ...
    def __init__(self, x1, y1, x2, y2):
        ...

it:

    Executes the body top to bottom.
    Each def just creates a function object and assigns it as an attribute on the class being built.

So after the class statement is done, you end up with a Rectangle that has both:

    a Rectangle.overlaps method
    a Rectangle.__init__ method

The order of those two defs doesn’t matter for calling them later. When you write:

r = Rectangle(1, 2, 3, 4)

Python looks up Rectangle.__init__ on the finished class; it doesn’t care that overlaps was listed first.

The only time order inside the class would really matter is if you tried to do something like:

class Rectangle:
    print(__init__)  # This would fail if __init__ isn't defined yet
    def __init__(...):
        ...

But normal methods calling each other or being called from outside are fine, regardless of their order in the class.
How this ties back to your concern

    When you write self.__hit_box = Rectangle(...) in Dragon.__init__, that happens only when a Dragon object is created at runtime, not when Python is first reading the file.
    By the time any Dragon is instantiated, the whole file has been executed top-to-bottom, so the Rectangle class (with both __init__ and overlaps) is already fully defined.

So:

    Yes, the file runs top to bottom.
    But within class Rectangle, the order of def __init__ vs def overlaps doesn’t affect your ability to call them later. They both exist on the class once the class statement finishes.

Example of polymorphism with double inheritance:

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

