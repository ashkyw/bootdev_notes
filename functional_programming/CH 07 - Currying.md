# Currying

Function [currying](https://en.wikipedia.org/wiki/Currying) is a specific *kind* of function transformation where we translate a single function that accepts multiple arguments into multiple *functions* that each accept a *single* argument.

This is a "normal" 3-argument function:

```py
box_volum(3,4,5)
```

This is a "curried" *series of functions* that does the same thing:

```py
box_volume(3)(4)(5)
```

Another example that includes the implementations:

```py
def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3
```

And curried:

```py
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3
```

The `sum` function only takes a *single* input, `a`. It returns a *new* function that takes a single input, `b`. This new function when called with a value for `b` will return the sum of `a` and `b`. 
