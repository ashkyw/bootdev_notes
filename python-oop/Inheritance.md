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
