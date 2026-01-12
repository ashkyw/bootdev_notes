Inheritance - https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming]

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

Use a constant (e.g. MAX_HP = 100) when a value is:

    Magic-looking
        If a number/string appears and isn’t self-explanatory (3, 0.07, "us-east-1"), consider a named constant.
        Example: TAX_RATE = 0.07 is clearer than price * 0.07.

    Used in multiple places
        If the same value appears in more than one spot, make it a constant so you can update it in one place and avoid inconsistencies.

    Represents a domain concept
        If the value has meaning in your game/app (like MAX_INVENTORY_SIZE, TRIPLE_SHOT_COST, STARTING_GOLD), it deserves a name.

    Intended to be configuration, not logic
        Values that might change between environments or game balance tweaks should be constants: API URLs, default timeouts, difficulty tuning numbers.

    Should never change at runtime
        If the value is fixed for the whole run of the program, a constant signals “do not mutate this.”

    Needed across multiple modules
        Shared, stable values (like DEFAULT_PORT, SECONDS_PER_MINUTE) are good constant candidates.

On the flip side, avoid constants when:

    The value is truly one-off and obvious (range(3) in a tiny local loop, etc.).
    The value is derived from other values and better expressed as an expression than a stored constant.
    The value is meant to change frequently at runtime (that’s state, not a constant).

Inheritance in tree form. Archer and Wizard inherited from Hero:

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage

class Archer(Hero):
    ARROW_DAMAGE = 10

    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(self.ARROW_DAMAGE)
        
class Wizard(Hero):
    WIZARD_SPELL_DAMAGE = 25
    
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise Exception("not enough mana")

        self.__mana -= 25
        target.take_damage(self.WIZARD_SPELL_DAMAGE)

Another example, with cartesian grid maff!:

class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):        
        if x_1 <= self.pos_x <= x_2 and y_1 <= self.pos_y <= y_2:
            return True
        
        return False

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_hit = []
        x_1 = x - self.__fire_range
        y_1 = y - self.__fire_range
        x_2 = x + self.__fire_range
        y_2 = y + self.__fire_range
        for unit_name in units:
            if unit_name.in_area(x_1, y_1, x_2, y_2):
                units_hit.append(unit_name)

        return units_hit

Dragon fight! With list modification and efficent method:

def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    for dragon in dragons:
        describe(dragon)

    for i in range(0, len(dragons)):
        dragon = dragons[i]
        other_dragons = dragons.copy()
        del other_dragons[i]
        dragon.breathe_fire(3, 3, other_dragons)

def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print("====================================")
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        print("------------------------------------")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()

More OOP with double inheritance and setting super to a variable:

class Siege:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, food_price):
        return (distance / self.efficiency) * food_price

    def get_cargo_volume(self):
        pass


class BatteringRam(Siege):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        super().__init__(max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, food_price):
        base_cost = super().get_trip_cost(distance, food_price)
        return base_cost + (self.load_weight * 0.01)

    def get_cargo_volume(self):
        return self.bed_area * 2.0


class Catapult(Siege):
    def __init__(self, max_speed, efficiency, cargo_volume):
        super().__init__(max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume

