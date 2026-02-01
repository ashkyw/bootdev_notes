Since each .py file is a module we can easily group related functions, variables, and classes together in a module.
Then we can import using:

```py
  from module_name import my_function
  import module_name #for full import
```

Games often have a lot of magic numbers to represent various attributes: speed, item costs, attack damage
We'll use a dedicated module to store those constants.

The Greek letter delta (Δ) is often used to represent a change in a value in mathematics. 
In game development, we use "delta time" to represent the amount of time that has passed since the last frame was drawn. 
This value is useful to decouple the game's speed from the speed it's being drawn to the screen.The Greek letter delta (Δ) is often used to represent a change 
in a value in mathematics. 

In game development, we use "delta time" to represent the amount of time that has passed since the last frame was drawn. 
This value is useful to decouple the game's speed from the speed it's being drawn to the screen.

The Group class is a container that holds and manages multiple game objects. We can organize our objects into various groups to track them more easily.

You can think of them as a sort of Venn diagram. An object can be in multiple groups at the same time!

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/groups.png "Pygame Groups")


Examples of Using Groups

Create a new empty group called my_group:

```py
my_group = pygame.sprite.Group()
```

Add all future instances of a Player class to two different groups (group_a and group_b):

Player is the name of the class, not an instance of it
This must be done before any Player objects are created

```py
Player.containers = (group_a, group_b)
```

You can iterate over objects in a group just like any other collection in Python:

```py
for thing in group:
    thing.do_something(some_value)
```

You may also call the .update() method for every member of a group by calling it on the group itself:

```py
group.update(dt)
```

Examples of Using Groups

Create a new empty group called my_group:

```py
my_group = pygame.sprite.Group()
```

Add all future instances of a Player class to two different groups (group_a and group_b):

Player is the name of the class, not an instance of it
This must be done before any Player objects are created

```py
Player.containers = (group_a, group_b)
```

You can iterate over objects in a group just like any other collection in Python:

```py
for thing in group:
    thing.do_something(some_value)
```

You may also call the .update() method for every member of a group by calling it on the group itself:

```py
group.update(dt)
```
# [Splat operator](https://www.bitecode.dev/p/the-splat-operator-or-args-and-kwargs?open=false#%C2%A7unpacking-arguments)

Using the `*` allows us to unpack wrapped items such as tuples and dictionaries.
* `*` = unpack Tuples
* `**` = unpack dictionaries

Example of Splat operator
```py
def configure_plugin_decorator(func):
    def wrapper(*args):
        dict_args = dict(args)
        return func(**dict_args)
# unpack dict_args in func call
    return wrapper
```
