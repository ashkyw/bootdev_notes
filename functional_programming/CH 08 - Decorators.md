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
