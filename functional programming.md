Example of imperative code:

```py
car = create_car()
car.add_gas(10)
car.clean_windows()
```

Example of functional code:

```py
return clean_windows(add_gas(create_car()))
```

Tuples are immuatble. Example of creating a new tuple and adding that to existing tuple:

```py
ages = (16, 21, 30)
more_ages = (80,) # note the comma! It's required for a single-element tuple
# 'all_ages' is a brand new tuple
all_ages = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)
```

Another example of tuples:

```py
def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents

```
