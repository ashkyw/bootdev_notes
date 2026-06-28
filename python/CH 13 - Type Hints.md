# Type Hints

Some functions accept numbers as arguments; others accept strings. Some return lists; others return dictionaries, booleans or `None`.

When a program is small, you can _usually_ remember the types of your variables. But as programs grow, it's easy to forget:
  * Is `level` an `int` or a `str`?
  * Does `get_item()` always return an item name (`str`) or sometimes `None` if it can't find one?
  * Is `inventory` a list of strings, or a dictionary of item counts?

[Type hints](https://docs.python.org/3/library/typing.html) let us wirte those expectations directly in our code:
```py
def get_damage(weapon: dict, level: int) -> int:
  return weapon["damage"] + (level * 2)
```
The `weapon: dict`, `level: int` and `-> int` parts are type hints. They tell humans _and_ code editors what kinds of values the function expects and returns.

Type hints _don't make Python stop being Python_. It's still a dynamically typed language, and it won't automatically reject the wrong value just because a type hint says so.

Type hints are for:
* Making the code easier to read
* Helping your editor autocomplete and warn you about mistakes
* Making bugs easier to spot before running your code

# Basic Types

To add a type hint to a variable declaration, put a colon after the variable name, then the type. This comes _before_ the equals sign and the value:
```py
character_name: str = "Sir Galahad"
character_level: int = 7
character_health: float = 72.5
has_magic: bool = True
```
_The values work the exact same way they did before._ In fact, when it comes to simple variable declarations like this, you don't actually _need_ the hint. In this example:
```py
character_health = 72.5
```
Because `character_health` is assigned the value of `72.5`, your tooling can _infer_ that it's a `float`. That said, if you also want to _see_ the type name, you can optionally add it.

### Assignment
**Fix the type hints for each variable**
* `character_health` should be `str`
* `character_level` should be `int`
* `character_health` should be `float`
* `has_magic` should be `bool`
```py
# End of lesson code

character_name: str = "Gandalf"
character_level: int = 80
character_health: float = 99.5
has_magic: bool = True
```
#  Function Parameters

Function parameters can have type hints too! The syntax is the same as variable type hints: put a colon after the parameter name, then the type.
``` py
def greet_player(name: str):
 print(f"Welcome, {name}!")
```
When a function has multiple parameters, each one can have its own type hint:
``` py
def add_gold(current_gold: int, found_gold: int):
 return current_gold + found_gold
```
While adding a type to a variable declaration like:
``` py
character_health: float = 72.5
```
is considered a bit redundant due to type inference, adding type hints to function parameters is _not_ redundant. If you don't add them, your tooling won't know what types the function expects, which makes autocomplete and error checking less effective.

### Assignment
* Add a `str` type hint to `name`
* Add an `int` type hint to `level`
* Add a `float` type hint to `health`
* Add a `bool` type hint to `has_magic`

``` py
# End of lesson code
def get_character_status(name: str, level: int, health: float, has_magic: bool):
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status
```

#
