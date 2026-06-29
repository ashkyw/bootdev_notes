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

# Return Types

You can also annotate the type that you expect a function to return. When you know what types go into and come out of a function, you can (probably) use it without having to read every line of the function body. Return types come after the parameter list, before the colon:
```py
def add_gold(current_gold: int, found_gold: int) -> int:
    return current_gold + found_gold
```
The `-> int` means this function expects to return an integer
> [!TIP]
> **The syntax is a bit different** from type hints on variables and parameters: we use `->` instead of `:`, and there's no variable name before the type hint. This is because it doesn't really matter what name (if any) the function uses internally for the return value; we just care about the type.

Here's another example:
```py
def get_greeting(player_name: str) -> str:
    return f"Welcome, {player_name}!"
```

### Assignment
* Add a `str` return type hint to `get_item_description`
```py
# End of lesson code
def get_item_description(item_name: str, damage: int, is_magical: bool) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description
```

# Fixing Type Hints

The whole point of type hints is that they should **match what the code actually does**. If a function returns a string, its return type hint should also be `str`.
```py
def get_quest_reward(quest_name: str, quest_xp: int) -> str:
    return f"You've earned {quest_xp} XP for completing the {quest_name} quest!"
```
An incorrect type hint is confusing at best, even if you can still force the Python code to run. Your editor will likely also warn you, with something like a red squiggly line, if a function returns a value that doesn't match its return type hint.

### Assignment
* Fix the return type of `get_greeting`
```py
def get_greeting(player_name: str) -> str:
    return f"Welcome to Fantasy Quest, {player_name}!"
```

# List and Set Hints
We've covered hints for **basic types** like `str`, `int`, `float`, and `bool`, but you can also add hints for container types: types that _hold other values_. For example:
* List
* Set
* Dict
* Tuple

When we type-hint a container, we specify what kind of container it is _and_ what type of values it contains. For example, a _list_ of _strings_ can be expressed as `list[str]`
```py
inventory: list[str] = ["Iron Sword","Healing Potion"]
```
The "contained" type goes in square brackets after the container type. Similarly, for a _set_ of _strings_, we would write `set[str]`:
```py
unique_items: set[str] = {"Iron Sword","Healing Potion"}
```
### Assignment
* Add a `list[str]` to the inventory parameter
* Add a `set[str]` return type hint
```py
def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items
```
# Dictionary Hints
Dictionaries are container types too, but they map keys to values, so their type hints include both:
```py
item_counts: dict[str, int] = {
 "Wooden Arrow": 30,
 "Small Amethyst": 2,
}
```
The first type is for the keys; the second is for the values.
```py
dict[key_type, value_type]
```
So `dict[str, int]` means:
* The keys are strings
* The values are ints

> [!TIP]
> Not all types can be used as dictionary keys. The key types that you'll see most often are strings and integers. Dictionary valuse, on the other hand, can be any type.

### Assignment
* Add a `dict[str, int]` to the `item_counts` parameter
* Add `str` to the `item_name` parameter
* Add an `int` return type hint
```py
# End of lesson code
def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0
```
# Tuple Hints

Lists and sets _usually_ hold multiple values of the same type:
```py
inventory: list[str] = ["Black Knight Halberd", "Skull Lantern", "Notched Whip"]
```
But tuples are a **small fixed group of values** where each position has its own meaning. Because they're fixed, it's quite common for those values to be of different types. For example, a loot drop might have an item name and a quantity:
```py
drop: tuple[str, int] = ("Garnet Mark", 2)
```
`tuple[str, int]` means:
 * There are two values in the tuple
 * The first value is a string
 * The second value is an integer

A tuple can have any number of values -- though `2` and `3` are the most common. Here's an example representing a character's HP, MP and stamina:
```py
stats: tuple[int, float, int] = (100, 42.5, 75)
```
The type hint `tuple[int, float, int]` tells us this is a three-value tuple with an integer, a float and another integer.

### Assignment
* Add an `int` type hint to the `enemy_level` parameter
* Add a `tuple[str, int]` return type hint
```py
def get_loot_drop(enemy_level: int) -> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3
```
# Specific Container Types
It's possible to type-hint a container with _just_ the container type:
```py
items: list = ["Black Firebomb", "Titanite Chunk"]
```
This says `items` is a list, but it doesn't tell us what _kind of values_ go inside! Assuming you know what's inside, best to be specific:
```py
items: list[str] = ["Black Firebomb", "Titanite Chunk"]
```
That said, bare container type hints aren't _wrong_. Sometimes you really _don't know_ what types of values a container will hold, or the specific type hint would be too complicated to be useful. You'll see that occasionally with `dict`s. Just give clear type hints whenever possible.

### Assignment
* Update `items` from `list` to `list[str]`
* Update `item_counts` from `dict` to `dict[str, int]`
* Update return type from `tuple` to `tuple[str, int]`
```py
def get_reward_summary(items: list[str], item_counts: dict[str, int]) -> tuple[str, int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items
```
