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

2. **The `union` is the clever part.** A union lets one field store _one_ of  several types in the same memory slot. The `kind` field is the tag that tells us which member is currently valid. The pairing of an enum tag plus a union is called a **tagged union**, and is a common way to build dynamic-type systems.

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
    * If it falis, return `NULL`
    * Set the `kind` field to the appropriate enum
    * Store the float value in the object
    * Return the pointer

```C
// End of lesson .c file

// End of lesson .h file
```
## Notes from the boots AI
