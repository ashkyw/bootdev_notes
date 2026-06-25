# Handling Cycles

We built a simple reference garbage collector. It can handle:
* Simple types like `INT` and `FLOAT`
* Dynamically allocated types like `STRING`
* Static Container types, like `VECTOR3`
* Dynamic container types, like `ARRAY`

However, there's a problem with our implementation. Look at this code:
```C
snek_object_t *first = new_snek_array(1):
snek_object_t *second = new_snek_array(1):
// refcounts: first = 1, second = 1
snek_array_set(first, 0, second);
// refcounts: first = 0, second = 1
refcount_dec(second);
// refcounts: first = 0, second = 0
// all free!
```
We create a `first` array, and shove the  `second` array inside of it. Everything here works as expected. The trouble arises when we introduce a cycle: for example,  `first` contains `second`, but `second`also contains `first`...

### Assignment
Run the code in its current state. Notice that the assertions in `main.c` _fail_. Even though we decremented both the `first` and `second` arrays' refcounts, neither was freed: the refcounts are not `0`!

Fix the _assertions_ to pass by updating them to match the sad reality of our current implementation.

**Observe**

The reason both refcounts are stuck at `1` after being decremented is that, when `first` has its refcount decremented, it already has `2`. So it only drops to `1`, which does _not_ trigger a "free" of the `second` array:
```C
void refcount_dec(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount--;
  if (obj->refcount == 0) {
    // this doesn't happen when refcount is 1
    return refcount_free(obj);
  }
  return;
}
```
And because `second` still has `2` refcounts, it also only drops to `1`, which fails to trigger a "free" of the first array. In other words, we have a cycle, and our simple reference counting garbage collector can't handle it.
 **NOTE:** This assignment we just updated the unit tests to force the current implementation to work.
```C
// End of lesson .c file

#include "bootlib.h"
#include "munit.h"
#include "snekobject.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, correctly_free, {
  snek_object_t *first = new_snek_array(1);
  snek_object_t *second = new_snek_array(1);
  // refcounts: first = 1, second = 1
  snek_array_set(first, 0, second);
  // refcounts: first = 1, second = 2
  snek_array_set(second, 0, first);
  // refcounts: first = 2, second = 2
  refcount_dec(first);
  refcount_dec(second);
  assert_int(first->refcount, ==, 1, "Refcount first should be ?");
  assert_int(second->refcount, ==, 1, "Refcount second should be ?");
});

// Don't touch below this line

int main() {
  MunitTest tests[] = {
      munit_test("/correctly_free", correctly_free),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("refcount", tests);

  int result = munit_suite_main(&suite, NULL, 0, NULL);

  printf("*** NOTE: A memory leak warning is EXPECTED here ***\n");
  printf("*** We'll fix the circular reference problem soon ***\n");

  return result;
}

```
# Pros and Cons

To solve our cyclic reference issue (and to force us to implement another GC algorithm) we're going to implement a [mark and sweep](https://en.wikipedia.org/wiki/Tracing_garbage_collection#Na%C3%AFve_mark-and-sweep) garbage collector. 

### Pros of MaS
* Can detect cycles, and prevent memory leaks in certain cases.
* Less on-demand bookkeeping
* Reduces potential performance degradation in highly multithreaded programs (refcounting requires atomic updates for thread safety)

### Cons of MaS
* More complex to implement (we're fixin' to find out)
* Can cause "stop-the-world" pauses when lots of objects exist and must be freed (resulting in poor performance)
* Reduces potential performance degradation in highly multithreaded programs (refcounting requires atomic updates for thread safety)
* Less predictable performance

### Assignment
We'll be using a `vm_t` struct which stands for `Virtual Machine Type`. This `vm_t` simulates what would normally be tracked if Sneklang were a fully functional interpreted language. This virtual machine is much simpler than a real one because all we care about is demonstrating the garbage collection aspects.

Open `vm.h` and take a look at the `vm_t` struct. The `frames` field holds a stack of frames, which are pushed and popped as we enter and exit new scopes. For example:
```py
msg1 = "This is in scope 1"
def outer_func():
    msg2 = "This is in scope 2"
    def inner_func():
        msg3 = "This is in scope 3"
        return
    return
```
At each of the `scope` entrances (in this case function calls), a new stack frame is pushed onto the `frames` stack. When we exit a scope (a function returns), we pop the stack frame off the `frames` stack. Because we use `void *` to work with generics in C, you can't actually tell what the data type held by the `stack_t` is for each field. We'll write some wrapper functions later to help us make sure that we don't accidentally push the wrong kinds of data into our stacks.

1. `objects` field is also a stack, but it holds `snek_object_t` pointers.
  * Allocate space for a `vm_t` struct on the heap
  * Initialize the `frames` stack with a capacity of `8` and the `objects` stack with a capcity of `8` using the `stack_new` function
  * Return a pointer to the new `vm_t` struct
2. Complete the `vm_free` function
  * Free the `frames` and `objects` stacks (remember, we wrote a special `stack_free` function)
  * Free the `vm_t` struct

```C
// End of lesson vm.c file
#include "vm.h"

vm_t *vm_new() {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  if (vm->frames == NULL) {
    free(vm);
    return NULL;
  }

  vm->objects = stack_new(8);
  if (vm->objects == NULL) {
    stack_free(vm->frames);
    free(vm);
    return NULL;
  }

  return vm;
}

void vm_free(vm_t *vm) {
  if (vm == NULL) {
    return;
  }

  stack_free(vm->frames);
  stack_free(vm->objects);

  free(vm);
}

// See CH 11 - Mark and Sweep GC Codebase.md for additional files
```
# Stack Frames

Think back to the warnings about working with `void *` data types. It's easy to push the wrong kinds of data onto our `stack_t` because it will let _anything_ in.

To prevent us from footgunning, we will create some functions that are more type safe and make it much more difficult to do the wrong thing when interacting with our `vm_t`. Wrong things like:

```C
// The C compiler won't stop us
stack_push(vm->frames, (void *)7);
stack_push(vm->frames, (void *)"uh oh");
```
But we want to make it easier on ourselves to only push `frame_t *` types onto `vm->frames`, so we'll write some wrapper functions to help us out

### Assignment

Look at the `frame_t` type in `vm.h`. It's a simple struct that holds a `stack_t` of `snek_object_t *` pointers that represent the object references in the frame.
1. Complete the `vm_frame_push` function in `vm.c`. It should `stack_push` a `frame_t *` onto the `vm->frames` stack
2. Complete the `vm_new_frame` function in `vm.c`. It should:
  * Allocate a new `frame_t` on the heap
  * Initialize the frame's references with a `stack_new` capacity of `8`
  * Push the newly allocated frame onto the `vm->frames` stack
  * Return the new frame
3. Complete `frame_free` in `vm.c`
  * Free the `frame_t`'s `references` stack (we have a function for this)
  * Free the `frame_t` struct

```C
// End of lesson vm.c file
#include "vm.h"

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *frame = malloc(sizeof(frame_t));
  frame->references = stack_new(8);

  vm_frame_push(vm, frame);
  return frame;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

// don't touch below this line

vm_t *vm_new() {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_free(vm_t *vm) {
  for (int i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);
  stack_free(vm->objects);
  free(vm);
}
// See CH 11 - Mark and Sweep GC Codebase.md for additional files
```
