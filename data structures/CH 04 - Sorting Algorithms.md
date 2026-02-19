# Sorting Algorithms

Almost every action you take in a web app relies on sorted data. Just looking up a user's profile in a database likely relies on a sorted index (which we'll talk about in another course).

Fortunately, most programming languages provide their own standard sorting implementation. In Python, for example, we can use the `sorted` function:

```py
items = [1, 5, 3]
print(sorted(items)) # [1, 3, 5]
```
