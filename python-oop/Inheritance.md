(Inheritance)[https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming]

first code snippets Example of what code would look like without inheritance, we write the same code twice:

class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height += self.speed

class Helicopter:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self):
        self.height += self.speed

    def rotate(self):
        self.direction += 90

second code snippet example of what code looks like with inheritance, we take the aircraft class and pass it into the helicopter class, then act upon itself.

class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90

Another example of inheritance:

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows
        
    def get_num_arrows(self):
        return self.__num_arrows
Another example:

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

    def use_arrows(self, num):
        if self.__num_arrows < num:
            raise Exception("not enough arrows")
        self.__num_arrows -= num

class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        use_arrows = 3
        self.use_arrows(use_arrows)
        return f"{target.get_name()} was shot by 3 crossbow bolts

Explanation on constants and good hygiene:

Where magic numbers really matter is when:

    The same number is used in multiple places, or
    The meaning isn’t obvious from context.

A more “hygienic” version, if you want to be disciplined, would be a named constant at class level:

class Crossbowman(Archer):
    TRIPLE_SHOT_COST = 3

    def triple_shot(self, target):
        self.use_arrows(self.TRIPLE_SHOT_COST)
        return f"{target.get_name()} was shot by 3 crossbow bolts"

Now the “3-ness” has a clear name and is easy to change.

So:

    self.use_arrows(3) – acceptable and simple here.
    use_arrows = 3 local variable – meh, not harmful, but not adding much clarity.
    TRIPLE_SHOT_COST = 3 as a constant – best style if you want to practice good habits.
Use a constant when:

    The value has a meaningful concept (not just “3” but “cost of a triple shot”).
    You don’t expect it to vary per object, only per class/module.
    It might be used in multiple places, or you want to avoid hunting down the number later.

So in this case:

    “Triple shot always uses 3 arrows” → conceptually stable.
    It belongs to the idea of a Crossbowman’s ability, not to each specific instance’s state.

That makes a class-level constant a great fit:

class Crossbowman(Archer):
    TRIPLE_SHOT_COST = 3  # constant

    def triple_shot(self, target):
        self.use_arrows(self.TRIPLE_SHOT_COST)
        return f"{target.get_name()} was shot by 3 crossbow bolts"

In larger programs you’ll see similar patterns:

MAX_HP = 100
CRIT_MULTIPLIER = 1.5
DEFAULT_ARROW_COUNT = 10

