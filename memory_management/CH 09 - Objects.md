# SnekObjects

Objects in C?!? No. Way.

However, our Sneklang is build in C, and everything in Sneklang is an "object". To be clear, not a _class_ or _object-oriented programming_ object, but a higher-level data structure that _holds some metadate about itself_.
For example:
  * What type of data it holds (int, float, string, etc.)
  * The size of the data it holds
  * The data itself
  * How many references to itself exist (at least later when we build the garbage collector)

That last item it critical. Sneklang is a garbage-collected language, we need to know how many references to an object exist so we can free it when it's no longer needed.

### Assignment
Complete the missing definitions in `snekobject.h`
* An enum called snek_object_kind_t with a single value `INTEGER`
* A union called snek_object_data_t with a single member, an integer named `v_int`
* A struct declaration called `snek_object_t` with two members:
  1. A member of type `snek_object_kind_t` named `kind`
  2. A member of type `snek_object_data_t` named `data`
```C
// End of lesson code
typedef enum SnekObjectKind { INTEGER } snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;
```
## Notes from the boots AI

A `union` lets multiple possible fields share the same memory space. Right now it only has one field, `v_int`, but later it could hold other types like floats, strings, etc.

Important distinction:
* A `struct` stores all its fields at once.
* A `union` stores one active field at a time.

##### `struct`
```C
typedef struct SnekObject {
 snek_object_kind_t kind;
 snek_object_kind_t data;
}
```
This creates a Sneklang object with: 
* `kind` tells you what type of object it is.
* `data` stores the actual value

This is a common C pattern for building dynamic language runtimes: use a `kind` field to describe what is inside a generic data field.

#  Integer

Let's start with a single integer object. The difference between a "snek integer" and a regular C integer is that the Snek integer:
1. Is allocated on the heap
2. Can store additional metadata about itself (for now, just its type)

### Assignment
Complete the `new_snek_integer` function.
* Use `malloc` to allocate heap memory for a new pointer to a `snek_object_`
* If it fails, return NULL
* Set the `kind` field of the new snek object to the `INTEGER` enum value
* Set the `v_int` field of the new snek object to the integer value passed in.
* Return the pointer to the new snek object
```C
// End of lesson code

#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}
```

## Notes from the boots AI
1. **`malloc` returns raw, unintialized memory.** It provides a chunk of memory large enough for whatever type you're working with, but the bytes are garbage values until we set them. That's why we specify both `kind` and `data.v_init`.

2. **The `union` is the clever part.** A union lets one field store _one_ of  several types in the same memory slot. The `kind` field is the tag that tells us which member is currently valid. The pairing of an enum tag plus a union is called a **tagged union**, or , **discriminated union** and is a common way to build dynamic-type systems.

#Float

Sneklang needs floats (naturally). How else will all the crypto bros write weird floating-point bugs into their smart contracts?

How do we store both floats and integers in the same type?

We're going to use `union` and `enum` features in C to be able to do this, just like we discussed in previous chapters. You will need te extend the existing `snek_object_kind_t` and `snek_object_data_t` types to be able to include both `int`s and `float`s (and we will continue to add more types in the following chapters).

### Assignment
You will need to edit 2 files in this lesson
1. `snekobject.h`
    * Add a new enum value to the `snek_object_kind_t` enum called `float`
    * Add a new `float` field to `snek_object_data_t` called `v_float`
    * Declare the `new_snek_float` function
2. `snekobject.c`
    * Allocate memory for a new pointer to a `snek_object_t`
    * If it fails, return `NULL`
    * Set the `kind` field to the appropriate enum
    * Store the float value in the object
    * Return the pointer

```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }
  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

// End of lesson .h file
typedef enum SnekObjectKind { 
  INTEGER,
  FLOAT,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
```
## Notes from the boots AI

**Why a `union` instead of a `struct`?** A `struct` would allocate memory for _all_ fields simultaneously. A `union` allocates only enough memory for it _largest_ member, and all fields share that same memory. This is a deliberate space optimization -- a snek object is either an int _or_ a float, never both at once.

**`unions` grow to accomdate**. On most platforms `sizeof(int) == sizeof(float) == 4`, so the union size won't change here. But, as we add more types (string, boolean, etc.), the union will grow to accomodate the largest member

**Enum ordering matters slightly**. `INTEGER` gets value `0` and `FLOAT` gets the value `1` by default. Zero-initialized memory would defalut to `INTEGER` kind -- something to be mindful of when debuggipg uninitialized objects.

# String
Now we're going to do our first object that has something... _additional_ allocated. When we allocate memory for a "snek object", that reserves memory for the object itself. Small data types like integers and floats are stored directly in the object, so there's no need for additional memory allocation.

Strings, however, are a different story. Strings in C are just arrays of characters, and because they can be any length, we need to dynamically allocate memory for the string data for the object itself.
```C
char *my_string = "hello world";
```
In the example above, `my_string` is a pointer to a character array. The character array contains
```C
h e l l o w o r l d \0
```
The extra spot at the end with the `\0` is the null terminator.

### Assignment
1. `snekobject.h`
    * Add a new enum value to the `snek_object_kind_t` enum called `STRING`
    * Add a new string (`char *`) field to `snek_object_data_t`
    * Declare the `new_snek_string` function
2. `snekobject.c`
    * Allocate memory for a new pointer to a `snek_object_t`
    * If it fails, return `NULL`
    * Calculate the length of the string (`strlen`)
    * Allocate memory in a `char *` equal to the length + 1 for `\0`
    * If allocation fails, free the memory allocated for the object
    * Copy the data from the input value into the new string field (`strcpy`)
    * Set the `kind` field
    * Return the pointer
```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  size_t len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

// End of lesson .h file
typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
```
## Notes from boots AI
**Why `strlen(value)+1`?**
`strlen` returns the number of characters _excluding_ the `\0`. You need to `+1` to allocate space for it, otherwise `strcpy` writes one byte past the end of you buffer -- classic undefined behavior

**Why copy at all?**
The caller owns the original `char *value`. If they later `free` or modify it, your object's string would become a dangling pointer or silently corrupt. By copying, the object owns its own memory and controls its own lifeline.

**`sizeof(char)` is always 1**
`sizeof(char)` is guaranteed to be `1` by the C standard. Writing `malloc(len)` is idiomatic and equally correct. The pattern `sizeof(T) * count` matters more for types like `int` or `struct`.

**The two-stage `malloc` pattern**
Notice the structure:
1. Allocate the object
2. Allocate the string
3. If step 2 fails, free step 1 before returning `NULL`

This is the foundation of manual memory management. Every allocation you make must have a corresponding `free` somewhere, and every failure path must clean up everything allocated so _far_ -- no more, no less.

**`strcpy` vs `memcpy`**
`strcpy` is fine here because you're dealing with a null-terminated string. If you were copying arbitrary binary data (which might contain embedded `\0` bytes), you'd use `memcpy` with an explicit byte count instead.

# Vector3

`Vector3` is going to be the first Snek Object that can hold a reference to another Snek Object. It's a collection type: a type that holds other types.

Arrays, lists, dictionaries, and sets are all examples of collection types. We won't implement all of those types in this course, but they each follow the same pattern we're establishing here.

`Vector3` is similar to a Python tuple that contains _exactly_ 3 "SnekObject" elements.

### Assignment
1. `snekobject.h`
    * Forward declare the `snek_object_t` at the top of the file. It will need to be used in a circular dependency between `snek_object_t -> snek_object_data_t -> snek_vector_t`.
    * Create a new `struct` called `snek_vector_t` that has three fields. Name the fields `x`, `y`, and `z`. Each field should be a Sneklang Object pointer (`snek_object_t *`)
    * Add a new enum value to the `snek_object_kind_t` enum called `VECTOR3`
    * Declare the `new_snek_vector3` function
     >! NOTE
     > The `v_vector3` field is not a pointer to a `vector3`; it's directly allocated inside the struct. We can do this because we know the size of the vector(it's only 3 pointers wide) in advance.
2. `snekobject.c`
    * If any of the inputs are `NULL` return `NULL`.
    * Allocate memory for a new pointer to a `snek_object_t` and if the allocation fails return `NULL`
    * Set the `kind` field to the appropriate enum
    * Initialize the `v_vector3` field of the new snek object so that its `x`, `y`, and `z` members point to the input objects (for example, by creating a `snek_vector_t` with those fields and assigning it to `v_vector3`)
    * Return the pointer

```C
// End of lesson .c file

// End of lesson .h file
```
## Notes from boots AI
