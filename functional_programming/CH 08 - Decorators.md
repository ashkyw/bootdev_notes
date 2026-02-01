# Decorators

Remember function transformations where a (higher-order) function takes a function and returns a function with new behavior? [Python decorators](https://docs.python.org/3/glossary.html#term-decorator) are just [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) around that. "Syntactic sugar" just means "a more convenient syntax".

```py
def vowel_counter(func_to_decorate):
    vowel_count = 0
    def wrapper(doc):
        nonlocal vowel_count
        vowels = "aeiou"
        for char in doc:
            if char.lower() in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        return func_to_decorate(doc)
    return wrapper

@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("What")
# Vowel count: 1
# Document: What

process_doc("A wonderful")
# Vowel count: 5
# Document: A wonderful

process_doc("world")
# Vowel count: 6
# Document: world
```

The `@vowel_counter` line is "decorating" the `process_doc` function with the `vowel_counter` function. `vowel_counter` is called once when `process_doc` is defined with the `@` syntax, but the `wrapper` function that it returns is called every time `process_doc` is called. That's why `vowel_count` is preserved and printed after each time.

# It's Just Syntactic Sugar

Python decorators are just another (sometimes simpler) way of writing a higher-order function. These two pieces of code are identical:
With Decorator
```py
@vowel_counter
def process_doc(doc):
    print(f"Document: {doc}")

process_doc("Something wicked this way comes")
```
Without Decorator
```py
def process_doc(doc):
    print(f"Document: {doc}")

process_doc = vowel_counter(process_doc)
process_doc("Something wicked this way comes")
```
Another example of decorator use:

```py
def file_type_aggregator(func_to_decorate):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
        result = func_to_decorate(doc, file_type)

        return result, counts

    return wrapper

@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: '{doc}'. File Type: {file_type}"
```

# Args & Kwargs

In Python, [*args and **kwargs](https://book.pythontips.com/en/latest/args_and_kwargs.html) allow a function to accept and deal with a variable number of arguments.

* `*args` collects positional arguments into a *tuple*
* `**kwargs` collects keyword (named) arguments into a *dictionary*

```py
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}
```
# Positional Arguments

Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:
```py
def sub(a, b):
    return a - b

# a=3, b=2
res = sub(3, 2)
# res = 1
```
# Keyword Arguments

[Keyword arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments) are passed in by name. *Order does **not*** matter. Like this:
```py
def sub(a, b):
    return a - b

res = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1
```
# A Note on Ordering

Any positional arguments *must come **before*** keyword arguments. This will *not* work:
```py
sub(b=3, 2)
```
Another example of args and kwargs:

```py
def args_logger(*args, **kwargs):
    for i in range(len(args)):
        print(f"{i + 1}. {args[i]}")
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")
```

# Decorators

The `*args` and `**kwargs` syntax is great for decorators that are intended to work on functions with different [signatures](https://developer.mozilla.org/en-US/docs/Glossary/Signature/Function)

Example

The `log_call_count` function below doesn't care about the number or type of the decorated function's (`func_to_decorate`) arguments. It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.
```py
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper
```

Another example of `*args` `*kwargs` and the `*` splat operator:

```py
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = list(map(convert_md_to_txt, args))

        def kwarg_item_to_txt(item_tuple):
            key, value = item_tuple
            return (key, convert_md_to_txt(value))

        converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))
        return func(*converted_args, **converted_kwargs)

    return wrapper
```
# lru_cache

[`lru_cache` from the `functools` module](https://docs.python.org/3/library/functools.html#functools.lru_cache) is an example of a decorator and an example of memoization.

`lru_cache` memoizes the inputs and outputs of the decorated function in a size-restricted dictionary. It speeds up repeated calls to a slow function with the same inputs. For instance, if the function reads from disk, makes network requests, or requires a lot of computation AND it is used repeatedly with the same inputs.

Here's an example from the Python documentation that perfectly illustrates how and why to use the `lru_cache` decorator:

```py
from functools import lru_cache

@lru_cache()
def factorial_r(x):
    if x == 0:
        return 1
    else:
        return x * factorial_r(x - 1)

factorial_r(10) # no previously cached result, makes 11 recursive calls
# 3628800
factorial_r(5)  # just looks up cached value result
# 120
factorial_r(12) # makes two new recursive calls, the other 11 are cached
# 479001600
```

Since the `factorial` function is recursive and the inputs are sequential numbers, it's called repeatedly with the same inputs. Without the cache, the function would be called 30 times. With `lru_cache`, the function is only called 13 times. While you don't often need to compute factorials, this example ties together how to use a decorator *and* memoization *and* recursion.

Another example of recursion and `lru_cache`:

```py
from functools import lru_cache


@lru_cache()
def is_palindrome(word):
    if len(word) < 2:
        return True
    first = word[0]
    last = word[-1]
    if first != last:
        return False
    trimmed_word = word[1:-1]
    return is_palindrome(trimmed_word)
```

You can stack decorators, and use currying with decorators.

```py
def to_uppercase(func):
    def wrapper(document):
        return func(document.upper())

    return wrapper

def get_truncate(length):
    def truncate(func):
        def wrapper(document):
            return func(document[:length])

        return wrapper

    return truncate

@to_uppercase
@get_truncate(9) # currying
def print_input(input):
    print(input)

print_input("Keep Calm and Carry On")
# prints: "KEEP CALM"
```

Observe that `to_uppercase` wrapped `get_truncate(9)`, and `get_truncate(9)` returned `truncate` which wrapped `print_input`, then `print_input` printed "KEEP CALM" from "Keep Calm and Carry On".

Another example of currying and decorators

```py
def replacer(old, new):
    def replace(decorated_func):
        def wrapper(text):
            return decorated_func(text.replace(old, new))

        return wrapper

    return replace
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#27;")

def tag_pre(text):
    return f"<pre>{text}</pre>"
```
