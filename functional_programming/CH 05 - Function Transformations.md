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

The `self_math` function takes a function that operates on two *different* paraments (e.g. `multiply` or `add`) and returns a new function that operates on *one* paramenter *twice* (e.g. `square` or `double`)
