# Low level stack

Making a stack data structure with generics in C. 

Step One:

```C
// End of lesson code
#include "snekstack.h"
#include <stdlib.h>

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}
```

## Notes from the boots AI
`void *` is the universal pointer

Any pointer type can be implicitly cast to and from `void *` in C. That's how `malloc` works--it returns `void *` when you assign it to whatever typed pointer you need. No explicit cast is required in C, unlike C++.

**Pointer arithmetic is type-aware**
```C
int *p = ...;
p + 1; // advances by sizeof(int) bytes
```
This is why `void *` can't be used for arithemetic directly--the compiler doesn't know the size of what it points to.

**`NULL`** is just zero.

`NULL` is typically defined as `(void *)0`. Dereferencing it is undefined behavior, which is why you always check `malloc`'s return value before using the pointer.

**The stack vs heap distinction matters**

Local variables live on the call stack and are automatically freed when the function returns. Anything you `malloc` lives on the heap and persists until you `free` it. Returning a pointer to a local variable is a classic bug.
```C
// WRONG - s is destroyed when function returns
stack_t *bad() {
  stack_t s;
  return &s;
}

// RIGHT - heap allocated, caller owns it
stack_t *good() {
  return malloc (sizeof(stack_t));
}
```
**Ownership and freeing order matter**

Notice in the tests, `s->data` is freed before `s` itself. That order is important--if you freed `s` first, you'd lose your only reference to `s->data` and leak that memory.

**`sizeof` on a pointer vs the thing it points to**
```C
sizeof(stack_t *) // size of the pointer itself (8 bytes on 64-bit)
sizeof(stack_t)   // size of the whole struct
```
These fundamentals will come up constantly as we build the garbage collector

# Stack Push

The `realloc` function is used to resize memory that was previously allocate with `malloc` or `calloc`. It takes a **pointer to the old memory** and the new size, and returns a pointer to the new memory:
```C
void *realloc (void *ptr, size_t size);
```
```C
int *smol_boi = malloc(10 * sizeof(int));
int *large_boi = realloc(smol_boi, 20 * sizeof(int));
```

Now we'll store some data in the stack. If the count reaches the capacity, we'll double the heap size for the new data.
```C
// End of lesson .c file

#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;
      return;
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

// don't touch below this line

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

// End of lesson .h file
#include <stddef.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);
void stack_push(stack_t *stack, void *obj);
```
## Notes from the boots AI
**1. Separate capacity from count**

  A stack (and many dynamic data structures) tracks two different things: how much memory is allocated (`capacity`) and how many elements are actually stored    (`count`).

**2. Doubling capacity is a classic amortized strategy**

  Doubling an overflow means reallocations happen rarely -- O(log n) times for n pushes. The total cost of all reallocations is O(n), so each push is O(1)       amortized. This is the same strategy used by C++ `std::vector` and many other dynamic arrays.
  
**3. Always use temp pointrs with `realloc`**
```C
void **temp = realloc(stack->data, new_size);
if (temp == NULL) {
  // recover gracefully
  return;
}
stack->data = temp;
```
  If you assign directly back to `stack->data` and `realloc` fails, you've just leaked the original memory -- `stack->data` becomes NULL and you've lost the     pointer to the old allocation

**4. Restore state on failure**

  When `realloc` fails, you rolled back `stack->capacity` to its previous value. This is the "leave things as you found them" principle -- the caller can        still use the stack safely after a failed push
  
**5. `void **` is an array of pointers**

   `data` being `void **` means each slot holds a `void *` -- a pointer to anything. This is how C implements generic containers without templates or generics.

# Stack Pop

Items go on and off the stack from the same end. (last in, first out).

The pop method is much simpler than the push method in this case, because we aren't worrying about resizing the stack.
```C
// End of lesson .c file
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }
  stack->count--;
  return stack->data[stack->count];
}

// don't touch below this line'

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;
      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

// End of lesson .h file
#include <stddef.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);
void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

```
## Notes from the boots AI

**LIFO (Last In, First Out)**

The stack's `count` acts as a "top of stack" pointer. The last pushed element lives at `data[count - 1]`, so decrementing `count` before returning gives you the correct element

**Why decrement _before_ indexing?**

After `stack->count--`, `count` now holds the index of the element you just "removed". This is a common C idiom -- the count doubles as the next-available index, so `count - 1` (post-decrement `count`) is always the top.

**No memory freeing needed**

Popping doesn't `free` the element -- the stack doesn't own the data, it just holds pointers to it. The caller is responsible for the liftime of the actual objects. 

**Empty Stack Guard**

 Always check `count == 0` before accessing the `data`. Accessing `data[-1]` (i.e., `data[count - 1]` when `count` is 0 and `count` is a `size_t`) would be undefined behavior -- and with unsigned types, `0 - 1` wraps around to a huge number.

**`void *` flexibility**
The stack works with any pointer type because it stores `void *`. The caller casts back to the appropriate type when popping. 

# Stack free

In C, we don't have a lot of abstractions at our disposal. There are no classes, destructors, functors, monads, made-up-category-theory-words, etc.

We've got _data_. And we've got _functions_.

So, to make it easier to work with our `Stack`, we're going to build our own little `free` function that will clean up all the memory that we've allocated for our stack.

### Assignment
Complete the `stack_free` function
  * If the stack is `NULL`, return immediately.
  * If the stack data is not `NULL`, free the stack data
  * Free the stack itself
  You can assume all the elements inside the stack are already freed. That's not _our_ problem.

```C
// End of lesson .c file
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

// don't touch below this line

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;
      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

// End of lesson .h file
#include <stddef.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);
void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);
void stack_free(stack_t *stack);

```
## Notes from the boots AI
**Order of freeing matters**

Always free inner allocations before outer ones. Here, `stack->data` is freed before `stack` itself. If you did it in reverse, you'd lose the pointer to `data` and leak memory.

**NULL guard before dereferencing**

Checking `stack == NULL` before accessing `stack->data` prevents a segfault. Dereferencing a NULL pointer is undefined behavior in C -- it's one of the most common crash causes.

**NULL guard before freeing**

Technically,`free(NULL)` is safe in C (it's a no-op), so the `if(stack->data != NULL)` check isn't strictly required. But it's a good defensive habit, and it signals intent clearly to future readers.

**Ownership and responsibility**

The function assumes elemnts inside the stack are already freed by the caller. This is a deliberate design decision -- `stack_free` owns the container, not the contents. Documenting this kind of ownership contract is important in C since there's no runtime safety net to catch mistakes.

**Symmetry with allocation**
`stack_new` calls `malloc` twice (once for the struct, once for `data`). `stack_free` calls `free` twice in reverse order. This symmetry is a useful mental model: every allocation needs a corresponding free, and cleanup mirrors construction.

# Dangerous Push

Up until now, even though we made our stack with `void *`, you'll notice that we've only stored plain old `int` pointers. You can actually store _anything_ in the stack, but this is usually a bad idea. 

Now we're going to push an `int *` and a regular `int` directly onto the stack (_bad_ idea). This is just to show you can store _anything_ in `void *`, even values that aren't pointers.

### Assignment
  * Push the value `1337` directly onto the stack using `stack_push`. You'll need to cast the value to a `void *`
  * Allocate memory for a new `int` on the heap
  * Set the value to which the address points to `1024`
  * Push the int pointer onto the stack using the `stack_push` function

```C
// End of lesson code
#include "snekstack.h"
#include "stdlib.h"

void scary_double_push(stack_t *s) {
  stack_push(s, (void *)1337);

  int *i = malloc(sizeof(int));
  *i = 1024;
  stack_push(s, i);
}
```
## Notes from the boots AI
#### Casting an integer to `void *`
```C
stack_push(s, (void *)1337);
```
This stores the _value_ `1337` directly in the pointer slot, not at a memory address. It works because on most modern platforms, `sizeof(void *) >= sizeof(int)`, so the bits fit. But it is technically implementation-defined behavior in C -- the standard doesn't guarantee it round-trips cleanly. 

**Why this is dangerous**

When you later retrieve the value:
```C
int value = (int) s->data[0]; // cast pointer back to int
int *pointer = s->data[1]; // treat as actual pointer, dereference it
```
The caller must _already know_ which slots hold raw integer values vs. actual heap pointers. There's no type information stored alongside the data. If you call `free()` on `s->data[0]` thinking it's a heap pointer, you'll corrupt memory or crash -- because `1337` is not a valid heap address.

#### The real-world lesson

This is exactly why typed generics (C++ templates, Rust generics, Go generics) exist. A `void *` stack is powerful but puts the entire burden of type safety on the programmer. In production C you'd typically:
  * Store only pointers to heap-allocated data (uniform ownership)
  * Or use a tagged union to track the type of each element alongside its value

The heterogeneous `void *` approach is mostly useful for understanding _why_ higher-level abstractions were invented.

# Multiple Types

So we saw that we _can_ push both `int` and `int *` types into the same stack (remember: **bad idea**).

In this example, we'll see that not only can you push values and pointers into the same stack, but you can also push different types of values into the same stack.

Once again, **bad idea**. The point of all this is:

##### _**C doesn't care what you put in memory, it's bytes all the way down**_

Fortunately, C doesn't let you do these conversions automatically, but it still lets you do them. When you're working with `void *`, you're working with raw memory addresses, and you can cast them to whatever you want.

### Assignment
Complete the `stack_push_multiple_types` function.
* Allocate memory on the heap for a `float` and set the value to which it's pointed to `3.14`.
* Push the `float` onto the stack using `stack_push`.
* Create a `char *` constant that points to the value: `sneklang is blazingly slow!`
* Get the length of the string for memory allocation (Remember to leave room for `\0`)
* Allocate memory for a `char *`
* Copy the value to the memory
* Push the pointer to the memory onto the stack using `stack_push`

#### Tip:

Don't forget to use the `string.h` library when working with `char *` types
```C
// End of lesson .c file

#include "snekstack.h"
#include "stdlib.h"
#include <string.h>

void stack_push_multiple_types(stack_t *s) {
  float *f = malloc(sizeof(float));
  *f = 3.14;
  stack_push(s, f);

  const char *string = "Sneklang is blazingly slow!";
  size_t len = strlen(string) + 1;

  char *c = malloc(sizeof(char) * len);
  strcpy(c, string);
  stack_push(s, c);
}
```

## Notes from the boots AI
* A `void *` can hold a pointer to any type, but it does **not** remember the original type. You must know what type to cast/use it as later
* Assigning / dereferencing a string pointer like `*dest = *src` copies only the first character. (pointer decay)
* Consider what types something returns and match accordingly. Example: `strlen()` return `size_t`
  ```C
  size_t len = strlen(str);
  ```
* If one allocation can fail, clean up earlier heap allocationns to avoid memory leaks.
* General Rule: `ptr` is the address, `*ptr` is the value at that address.
