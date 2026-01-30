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
