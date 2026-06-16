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

##### Notes from the boots AI
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
// End of lesson code

```
