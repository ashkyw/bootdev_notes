# Function Transformations

"Function transformation" is just a more concise way to describe a specicfic type of [higher order function](https://en.wikipedia.org/wiki/Higher-order_function). It's when a function takes a function (or functions) as input and returns a *new* function. For example:

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/function%20transformations.png)

```py
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# self_math is a higher order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func):
    def inner_func(x):
        return math_func(x, x)
    return inner_func

square_func = self_math(multiply)
double_func = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10
```

The `self_math` function takes a function that operates on two *different* paraments (e.g. `multiply` or `add`) and returns a new function that operates on *one* parameter *twice* (e.g. `square` or `double`)

Another example of using function transformations:

```py
def get_logger(formatter):
    def logger(first, second):
        print(formatter(first, second))
    return logger
```
Another example:

```py
def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_converter(filename, content):
        file_extension = filename.split(".")[-1]
        if file_extension in valid_formats:
            return conversion_function(content)
        raise ValueError("invalid file format")

    return inner_converter
```

# Why Transform?

Best use for transformation, and any advanced technique, is when they make code *simpler than it would otherwise be*

# Code Reusability

Creating varations of the same function dynamically can make it a lot easier to share common functionality. Take a look at the `formatter` example below. It accepts a "pattern" and returns a new function that formats text according to that pattern:

```py
def formatter(pattern):
    def inner_func(text):
        result = ""
        i = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func
```
Now new formatters can be easily created:
```py
bold_formatter = formatter("**{}**")
italic_formatter = formatter("*{}*")
bullet_point_formatter = formatter("* {}")
```
And then used like this:
```py
print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello
```

> [!Note] 
> [Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)

In the below example closure is used to pass the defined functions into the `get_filter_cmd()` function. Basically, as we're passing in functions filter_one and filter_two get set to those functions.
Due to closure, it means that `filter_one` & `filter_two` are now variables holding the functions passed in. Thus `filter_one` becomes `filter_one()`.
```py
def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            return filter_one(content)
        elif option == "--two":
            return filter_two(content)
        elif option == "--three":
            return filter_two(filter_one(content))
        else:
            raise Exception("invalid option")

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
```
