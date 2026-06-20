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
* Use `malloc` to allocate heap memory for a new pointer to a `snek_object_t`
* If it fails, return `NULL`
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

2. **The `union` is the clever part.** A union lets one field store _one_ of  several types in the same memory slot. The `kind` field is the tag that tells us which member is currently valid. The pairing of an enum tag plus a union is called a **tagged union**, or **discriminated union**, and is a common way to build dynamic-type systems.

# Float

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
> [!NOTE]
> The `v_vector3` field is not a pointer to a `vector3`; it's directly allocated inside the struct. We can do this because we know the size of the vector(it's only 3 pointers wide) in advance.
2. `snekobject.c`
    * If any of the inputs are `NULL` return `NULL`.
    * Allocate memory for a new pointer to a `snek_object_t` and if the allocation fails return `NULL`
    * Set the `kind` field to the appropriate enum
    * Initialize the `v_vector3` field of the new snek object so that its `x`, `y`, and `z` members point to the input objects (for example, by creating a `snek_vector_t` with those fields and assigning it to `v_vector3`)
    * Return the pointer

```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};
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

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
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

// End of lesson .h file
typedef struct SnekObject snek_object_t;

typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);

```
## Notes from boots AI
**Tagged vs Untagged**
In C a struct can have two names:
1. A tag (e.g., `SnekVector` in struct SnekVector {})
2. A typedef alias (e.g, `snek_vector_t`)

The tag is only necessary if you need to refer to the struct _before_ the typedef is complete, or recursively within itself. For example, `snek_object_t` needs a tag (`SnekObject`) because it's forward-declared at the top of the file:
```C
typedef struct SnekObject snek_object_t;
```
That forward declaration is needed to break the circular dependency: `snek_object_t` contains `snek_object_data_t`, which contains `snek_vector_t`, which contains pointers to `snek_object_t`. The compiler needs to know `snek_object_t` exists before it finishes defining it.

`snek_vector_t`, on the other hand, has no such circular dependency. Nothing needs to reference it before its definition is complete, so there's no need for a tag. An anonymous struct with just a typedef alias is sufficient:
```C
typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;
```
**Compound Literals**

`obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};` is a compound literal. It's a C feature that creates a temporary unnamed value of a given type inline.

The two parts:
* `(snek_vector_t)` -- the **type cast**, telling the compiler "create a value of this type"
* `{.x = x, .y = y, .z = z}` -- a **designated initializer**, setting named fields of that struct

So the full line:
```C
`obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};`
```
Is equivalent to:
```C
snek_vector_t temp = {.x = x, .y = y, .z = z};
obj-> data.v_vector3 = temp;
```
Just without the named temp variable. The `{}` is an initializer list, much like an array

**Forward declarations exist to break circular dependencies**

When type A contains type B which contains a pointer back to type A, the compiler needs a heads-up that type A exists before it finishes defining it. The pattern:
```C
typedef struct SnekObject snek_object_t; // forward declare
```
...placed _before_ the other type definitions is the standard C solution to this.

**Unions share memory**

`snek_object_data_t` is a `union`, not a `struct`. That means all its fields (`v_int`, `v_float`, `v_string`, `v_vector3`) occupy the _same_ memory. The union is only as large as its largest member. Setting obj->kind is what tells the rest of the program which field is actually valid at any given time.

**Vectors store references, not copies**

`snek_vector_t` holds _pointers_ to `snek_object_t`, not copies of them. This is why the `same_object` test works — when you mutate `i->data.v_int`, all three of `vec->data.v_vector3.x/y/z` reflect the change, because they all point to the same object in memory.

**No deep free needed here**

Because the vector only holds references (not ownership), freeing the vector doesn't require freeing `x`, `y`, or `z`. Each object is freed independently. Ownership semantics like this become critical in more complex memory management scenarios.

That last point about ownership is a theme that will keep coming up as the course progresses.

# Array

Let's add a dynamically sized arrry to Sneklang. We'll do it in multiple parts. First, we'll create an empty array.

### Assignment

1. `snekobject.h`
    * Add a new enum value to the `snek_object_kind_t` enum called `ARRAY`
    * Create a new struct called `snek_array_t` that has two fields
       1. `size`  -- the numebre of elements in the array, a `size_t`
       2. `elements` -- a pointer to an array of snek object pointers , `snek_object_t**`
    * Add a new `snek_array_t` field (the struct type just created) to `snek_object_data_t` called `v_array`
    * Declare the `new_snek_array` function
2. `snekobject.c`
    * Accept a `size` parameter
    * Allocate memory for a new pointer to a `snek_object_t`, if it fails return NULL
    * Allocate memory for a new pointer to an array of snek objects (`snek_object_t **`).
       1. How much memory should we allocate? Think about it: probably the `sizeof` a pointer for each element in the array. We're not storing the actual snek objects in the array, just pointers to them.
       2. If the allocation fails, `free` the first snek object allocation and return `NULL`
       3. Use [`calloc`](https://en.cppreference.com/w/c/memory/calloc) instead of `malloc` so there is no "junk" in our array to start. `calloc` takes two arguments, # of objects, size of each object
    * Set the `kind` field
    * Create a new `snek_array_t` struct, set `size` and `elements` fields
    * Set the `v_array` field of the new snek object to the newly created `snek_array_t`
    * Return the pointer
```C
// End of lesson .c file

#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
// Create new snek_array_t from new pointers
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

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

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
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

// End of lesson .h file

#include <stddef.h>

typedef struct SnekObject snek_object_t;

typedef struct {
  size_t size;
  snek_object_t **elements;
} snek_array_t;

typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3,
  ARRAY,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
  snek_array_t v_array;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(size_t size);
```

## Notes from boots AI
`calloc` vs `malloc`

`calloc(n, size)` is equivalent to `malloc(n * size)` followed by `memset(..., 0, ...)`. The zero-initialization is what guarantees your array slots start as `NULL` pointers rather than garbage values. For pointer arrays especially, this matters — dereferencing an uninitialized pointer is undefined behavior.

# Set

We can make empty arrays! Which is kinda pointless, but the bones are there. Let's make the array useful by allowing us to store values in them.

`snek_array_set` sets a value at a specific index in the array. The equivalent in Python would be 
```py
array[3] = new_value
```

### Assignment

* If the object or the new value is `NULL` return `false`
* If the object's `kind` is not `ARRAY`, return `false`
* If the index is out of bounds, return `false`. Rememeber `v_array` has a `size` field
* Return `true`
```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

bool snek_array_set(snek_object_t *snek_obj, size_t index,
                    snek_object_t *value) {
  if (snek_obj == NULL || value == NULL) {
    return false;
  }

  if (snek_obj->kind != ARRAY) {
    return false;
  }

  if (index >= snek_obj->data.v_array.size) {
    return false;
  }

  snek_obj->data.v_array.elements[index] = value;
  return true;
}

// don't touch below this line

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

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

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
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

// End of lesson .h file
#include <stdbool.h>
#include <stddef.h>

typedef struct SnekObject snek_object_t;

typedef struct {
  size_t size;
  snek_object_t **elements;
} snek_array_t;

typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3,
  ARRAY,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
  snek_array_t v_array;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(size_t size);
bool snek_array_set(snek_object_t *array, size_t index, snek_object_t *value);

```

## Notes from boots AI

**`size_t` is unsigned**

The `index` parameter is `size_t`, which is an unsigned integer type. This means it can never be negative -- but it also means you can't check `index < 0` as a guard, (it's always false and some compilers will warn you). The `>= size` check handles the upper bound; the type itself handles the lower.

**The `elements` field is a pointer-to-pointer (`snek_object_t **`)**

The array doesn't store the objects directly -- it stores _pointers_ to them. So assigning `elements[index] = value` stores the address of the `snek_object_t`, not a copy of it. This is important for memory management: the array doesn't own those objects, it just references them.

## **This just kinda goes here**

Fun thought:

C gave programmers direct, predictable control over memory with almost no overhead -- which is exactly what you want when you're writing operating systems, databases, or embedded firmware where every byte and cycle matters. That control is also why C is still dominant in those domains today, decades later.

Rust's rise makes sense as a natural evolution. It keeps that same low-level control and performance profile, but the compiler enforces memory safety at compile time through its ownership and borrow checker system. So you get C-like speed without the class of bugs that AddressSanitizer was catching in your code just now -- use-after-free, buffer overflows, data races. The compiler simply refuses to compile code that would cause them.

The tradeoff is that Rust has a steeper learning curve because you're essentially negotiating with the compiler about who owns what memory and for how long. But once it compiles, you have strong guarantees that C can't give you without external tooling.

The through-line is that understanding memory management in C -- which you're doing right now -- is one of the best foundations you can have before tackling Rust. The ownership model makes a lot more intuitive sense when you already know _why_ it exists.

# Get
Now that we can store values in arrays, we need a way to _retrieve_ them. `snek_array_get` returns the value at a specific index in the array. The python equivalent would be:
```py
print(array[7])
```

### Assignment
`snek_array_get`
* If the object is `NULL`, return `NULL`
* If the object's `kind` is not an `ARRAY`, return `NULL`
* If the index is out of bounds, return `NULL`
* Return the value in the `elements` array at the specified index.
```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *snek_array_get(snek_object_t *snek_obj, size_t index) {
  if (snek_obj == NULL) {
    return NULL;
  }

  if (snek_obj->kind != ARRAY) {
    return NULL;
  }

  if (index >= snek_obj->data.v_array.size) {
    return NULL;
  }

  return snek_obj->data.v_array.elements[index];
}

// don't touch below this line

bool snek_array_set(snek_object_t *snek_obj, size_t index,
                    snek_object_t *value) {
  if (snek_obj == NULL || value == NULL) {
    return false;
  }

  if (snek_obj->kind != ARRAY) {
    return false;
  }

  if (index >= snek_obj->data.v_array.size) {
    return false;
  }

  snek_obj->data.v_array.elements[index] = value;
  return true;
}

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

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

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
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

// End of lesson .h file
// See previous lesson
```
## Notes from boots AI
This lesson follows a classic C pattern: validate first, dereference second.

**Mental model**
Think of `snek_array_get` like a guarded lookup:
1. Is there an object at all?
  * `snek_obj == NULL` protects against dereferencing a null pointer. Without it, `snek_obj->kind` could crash the program
2. Is it the right kind of object?
  * `snek_obj->kind != ARRAY` checks if the object is an array before using `data.v_array`. Since `data` is a `union`, only the field matching the current `kind`  should be used
3. Is the requested index valid?
  * `index >= snek_obj->data.v_array.size` prevents out-of-bounds access. In C, array bounds are _not_ checked automatically. Accessing past the end of an array is undefined behavior.
4. If all checks pass, return the object pointer stored at that position
  * `return snek_obj->data.v_array.elements[index];` returns the stored pointer in that slot. It does _not_ copy the object. It returns the same `snek_object_t *` that was previously stored with `snek_array_set`.

**Empty slots will return `NULL`**
The array is created with:
```C
calloc(size, sizeof(snek_object_t *))
```
calloc zero-initializes the allocated memory. For pointer arrays, that means each slot starts as `NULL`
If nothing is stored at `elements[index]`, then `snek_array_get` naturally returns `NULL`.

# Length
Now that we have all sorts of Snek Objects (int, float, str, array) we need a convenient way to get the `length` of _any_ snek object. In Python it's as easy as:
```py
print(len(x))
```
As a python dev, you don't have to know the value of `x` ahead of time because Python keeps track of it under-the-hood for you. We want the same capability in Sneklang.

### Assignment
`snek_length`
* If input is `NULL`, return `-1` (failure code)
* `int`, size is always `1`
* `float` size is always `1`
* `string` size is the length of the string in bytes `strlen()`
* `VECTOR3` size is always `3`
* `ARRAY` size is stored in `v_array.size`
* If input is none of the above, return `-1`
```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

int snek_length(snek_object_t *obj) {
  if (obj == NULL) {
    return -1;
  }

  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    return 1;
  case STRING:
    return strlen(obj->data.v_string);
  case VECTOR3:
    return 3;
  case ARRAY:
    return obj->data.v_array.size;
  default:
    return -1;
  }
}

// don't touch below this line

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

bool snek_array_set(snek_object_t *array, size_t index, snek_object_t *value) {
  if (array == NULL || value == NULL) {
    return false;
  }

  if (array->kind != ARRAY) {
    return false;
  }

  if (index >= array->data.v_array.size) {
    return false;
  }

  array->data.v_array.elements[index] = value;
  return true;
}

snek_object_t *snek_array_get(snek_object_t *array, size_t index) {
  if (array == NULL) {
    return NULL;
  }

  if (array->kind != ARRAY) {
    return NULL;
  }

  if (index >= array->data.v_array.size) {
    return NULL;
  }

  return array->data.v_array.elements[index];
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

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

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
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

// End of lesson .h file
// No changes from two lessons previous.
```
## Notes from boots AI
**Switch statements**

When a `case` has no `break` (or `return`) before the next `case`, execution falls through to the next one. So stacking cases like this:
```C
case INTEGER:
case FLOAT:
  return 1;
```
...means: "if the kind is `INTEGER` _or_ `FLOAT`, `return 1`." The `INTEGER` case has nothing to execute and no break, so it falls straight through to `FLOAT`'s code.

A more explicit way to see fall-through in action is when you actually _want_ to accumulate behavior:
```C
switch (alert_level) {
  case 3:
    sound_alarm();   // falls through
  case 2:
    lock_doors();    // falls through
  case 1:
    log_event();
    break;
}
```
Here, level 3 triggers all three actions, level 2 triggers two, and level 1 triggers one.

The `default` case is worth adding as a habit — it's your safety net for unexpected values and silences compiler warnings about missing returns.

# Add

If you're familiar with Python, you'll be familiar with how Python objects can have an `__add__` method. It allows devs to specify custom logic for different types of objects. For example, adding two integers we want to behave like this:
```py
3 + 5
# 8
```
But with an array, we probably want it to work like this:
```py
[3] + [5]
# [3, 5]
```
### Assignment
`snek_add`. It accepts two pointers to `snek_object_t` objects ("a" and "b") and returns a pointer to a new `snek_object_t` object (the result of the sum):
* If either input is `NULL` return `NULL`
* If "a" is an integer
  1. If "b" is an integer, return a `new_snek_integer` with the sum of the two integers
  2. If "b" is a float, return a `new_snek_float` with the sum of the float and integer
  3. Anything else, invalid operation, return `NULL`
* If "a" is a float
  1. If "b" is an integer, return a `new_snek_float` with the sum of the float and integer
  2. If "b" is a float, return a `new_snek_float`  with the sum of the two floats
  3. Anything else, invalid operation, return `NULL`
* If "a" is a string:
  1. If "b" is not a string, invalid operation, return `NULL`
  2. Otherwise:
    1. Calculate the length of the new string by combining the length of the two strings (handling the null terminator)
    2. Allocate memory for a new temporary string using `calloc()`
    3. Use `strcat()` to append the data from a and then b to the temp string
    4. Create a `new_snek_string` from the temp string
    5. Free the memory for the temporary string and return the new string object

  
## Notes from boots AI
