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
 # Tracking Objects

 Our virtual machine needs to track every _Snek object_ that gets created.

 We are no longer going to track how many times an object is referenced, but instead check _at garbage collection_ time if each object is still referenced at all. If it is, keep it. If it's not, free it.

 ### Assignment
* In `vm.c` compelete the `vm_track_object`, which adds an object to our `vm->objects` stack in a more type-safe way.
* In `sneknew.c` update the `_new_snek_object` function. Before returning the newly allocated object it should ensure it's tracked by the VM.
```C
// End of lesson sneknew.c
#include "sneknew.h"
#include "snekobject.h"
#include "vm.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object(vm_t *vm) {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }
  vm_track_object(vm, obj);
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_array(vm_t *vm, size_t size) {
  snek_object_t *obj = _new_snek_object(vm);
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

snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(vm_t *vm, int value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;

  return obj;
}

snek_object_t *new_snek_float(vm_t *vm, float value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(vm_t *vm, char *value) {
  snek_object_t *obj = _new_snek_object(vm);
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

// End of lesson vm.c
#include "vm.h"
#include "snekobject.h"
#include "stack.h"

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
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

// See CH 11 - Mark and Sweep GC Codebase.md for additional files.
```
# Free

Recall the `refcount_free` function that you wrote in the previous chapter. It should have looked something like this:
```C
void refcount_free(snek_object_t *obj) {
  switch (obj->kind) {
    case INTEGER:
    case FLOAT:
      break;
    case STRING:
      free(obj->data.v_string);
      break;
    case VECTOR3: {
      snek_vector_t vec = obj->data.v_vector3;
      refcount_dec(vec.x);
      refcount_dec(vec.y);
      refcount_dec(vec.z);
      break;
    }
    case ARRAY: {
      snek_array_t *array = &obj->data.v_array;
      for (size_t i = 0; i < array->size; i++) {
        refcount_dec(array->elements[i]);
      }
      free(array->elements);
      break;
    }
  }
  free(obj);
}
```
### Assignment

Let's rewrite our free-ing logic for mark-and-sweep. Because the virtual machine is the one tracking objects, all of the `refcount_dec` work can be removed! There's some very cool tricks coming up for mark-and-sweep to manage this, but for now you can just trust that we'll correctly free any of the contained elements if they are no longer alive.

1. `snekobject.c` - complete `snek_object_free`
  * `INTEGER`, `FLOAT`, and `STRING` objects should all work the same as the refcount version (non-container types)
  * `VECTOR3` doesn't need to do _anything_ before freeing the object, because the mark-and-sweep will handle the contained objects
  * `ARRAY` should free the `elements` array, but not the objects themselves because the mark-and-sweep will handle that
2. `vm.c` - complete `vm_free`
  * Iterate over all the VM's frames and free them using `frame_free`
  * Free the `frames` stack itself using `stack_free`
  * Iterate over all the VM's objects and free them using `snek_object_free`
  * Free the VM the struct itself.

```C
// End of lesson vm.c
#include "vm.h"
#include "stack.h"

void vm_free(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_free(vm->objects->data[i]);
  }
  stack_free(vm->objects);
  free(vm);
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

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}

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

// End of lesson snekobject.c
#include "snekobject.h"

void snek_object_free(snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    free(obj->data.v_string);
    break;
  case VECTOR3: {
    break;
  }
  case ARRAY: {
    snek_array_t *array = &obj->data.v_array;
    free(array->elements);
    break;
  }
  }
  free(obj);
}
// See CH 11 - Mark and Sweep GC Codebase.md for additional files.
```
# Mark and Sweep
We have enough machinery in place to start thinking about the "Mark and Sweep" part of our garbage collector.

**The Algorithm**
Mark and Sweep garbage collection was first described by John McCarthy in 1960, primarily for managing memory in `((lisp))`. It's a two-phase algorithm:

1. **Mark Phase:** Traverses the object graph, marking all reachable objects.
2. **Sweep Phase:** Scan memory, collecting all unmarked objects, which are considered garbage.

Note! We don't keep track of how many times a particular object is referenced, like we did with reference counting! Instead, we keep track of which objects are referenced in each `stack frame` and then traverse our container objects looking for any other referenced objects. That's what "traverse the object graph" means – a fancy way of saying "look for objects".

### Assignment
```C
// End of lesson sneknew.c
#include "sneknew.h"
#include "snekobject.h"
#include "vm.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object(vm_t *vm) {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }
  obj->is_marked = false;
  vm_track_object(vm, obj);
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_array(vm_t *vm, size_t size) {
  snek_object_t *obj = _new_snek_object(vm);
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

snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(vm_t *vm, int value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;

  return obj;
}

snek_object_t *new_snek_float(vm_t *vm, float value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(vm_t *vm, char *value) {
  snek_object_t *obj = _new_snek_object(vm);
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

// End of lesson snekobject.h
#pragma once

#include "stack.h"
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
  bool is_marked;

  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

void snek_object_free(snek_object_t *obj);

```

# Frame References

Consider this example of Sneklang scopes and stack frames:
```py
msg1 = "This is in scope 1"
def outer_func():
    msg2 = "This is in scope 2"
    def inner_func():
        msg2 = "This is in scope 3"
        return
    return
```
In scope 2, we add `msg` to its referenced objects. Once again, this is a bit simplified from what you would do in a real, production-grade language, but the idea is the same.

Each stack needs to know about all of the objects that it references.

### Assignment
Complete the `frame_reference_object` function. It should push the object onto the stack of references for the current frame.
```C
// End of lesson vm.c
#include "vm.h"
#include "snekobject.h"
#include "stack.h"

void mark(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_t *frame = vm->frames->data[i];
    for (size_t j = 0; j < frame->references->count; j++) {
      snek_object_t *obj = frame->references->data[j];
      obj->is_marked = true;
    }
  }
}

// don't touch below this line

void frame_reference_object(frame_t *frame, snek_object_t *obj) {
  stack_push(frame->references, obj);
}

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
  // Free the stack frames, and then their container
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);

  // Free the objects, and then their container
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_free(vm->objects->data[i]);
  }
  stack_free(vm->objects);

  free(vm);
}

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

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}
```
## Notes from boots AI

When you write a long chain like:
```C
vm->frames->data[i]->objects[j]->references->is_marked = true;
```
At each `->`, the compiler asks: "What _type_ is the thing on the left, and does that type have this member?" The chain only works if every single hop lands on a real member of the real type at that point. You were guessing at the hops instead of checking them.

Walk it the way the compiler does:

* `vm` → `vm_t *`. Has `frames`. ✓
* `vm->frames` → `stack_t *`. Has data. ✓
* `vm->frames->data[i]` → `void *`. Stop. A `void *` has _no_ members at all. You then wrote `->objects`, but `void` isn't a struct, so that's already invalid. And even if it were a `frame_t`, `frame_t` has no member called `objects` — you invented it. Same with `references` and `is_marked` further down the chain.

So the one-liner wasn't "a valid trace written compactly." It was a trace that _skipped steps and assumed members existed_ without ever confirming the type at each hop.

The reason the named-variable version worked is that it forced two things:

1. **A cast/assignment that gives the `void *` a real type**. `snek_object_t *obj = frame->references->data[j];` tells the compiler "treat this `void *` as a `snek_object_t *`." Now `obj->is_marked` is checkable.
2. **One hop at a time.** You can't accidentally chain past a `void *` or invent a member, because each line is short enough to verify against the actual struct.

The takeaway: chaining isn't _wrong_ in C — `frame->references->count` is a perfectly good chain. The danger is chaining through a `void *` (which loses all type info) or chaining so far that you lose track of what type you're standing on. When either happens, break it into named, typed steps.

A `void *` is a "pointer to _something_, but I won't tell you what." It's deliberately type-less. That's _why_ the stack can hold anything — frames, objects, whatever — in the same `data` array. The flexibility comes at a cost: the compiler has thrown away the type info, so it won't let you do `->` on it. There's no struct to look members up in.

To use it, you re-attach a type:
```C
snek_object_t *obj = frame->references->data[j];
```
That assignment is the cast. In C, a `void *` converts to any object pointer type automatically, no explicit syntax needed. You could also write it explicitly:
```C
snek_object_t *obj = (snek_object_t *)frame->references->data[j];
```
Both do the same thing here. The point is: once it's typed as `snek_object_t *`, the compiler knows the layout, so `obj->is_marked becomes legal.

Here's the catch worth burning in: **the compiler doesn't verify your cast is correct.** If you'd written `frame_t *obj = frame->references->data[j];` it would _also_ compile — but you'd be lying about what's in there, and you'd get garbage or a crash at runtime. With `void *`, you are responsible for knowing what type actually lives in that slot. The stack just trusts you.

So the discipline is: the moment you pull something out of a `void *` container, immediately assign it to the correct typed variable.

# Trace

[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/tracing-in-mark-and-sweep-1920x1080.mp4)

## Lesson Notes

Now that we've done the first (and simplest) part: **marking**, we can trace through all of our objects and determine which ones are connected to the roots. For example
```py
def get_list():
  a = 5
  return [a]

print(get_list())
```
If we run this code it will return a list with the integer `a` inside of it. Our current `mark` function will mark the list, but it won't mark the integer `a`. Which means that when we go to sweep the memory, we will mark the list, but not the integer `a`. We'd then `free` `a` while it's still being used, and the operating system could then fill that memory with something else... which would be very bad! So, we need to prevent this.

But we also have another problem:
```py
def get_list():
  a = []
  a.append(a)
  return [5]

print(get_list())
```
In the above (very dumb) example, we create a list that references itself and then return a completely unrelated list. If our `trace` function looks for any object that is referenced by _any other object_ it will consider `a` alive because it has a reference (albeit, to itself in this case). In fact, `a` is unreachable because when `get_list` returns, `a` is no longer used anywhere.

_Tracing solves these problems_. To be clear, tracing is _part_ of the "mark" phase of mark and sweep. It's where we mark all the objects referenced by our root objects.

### Assignment
1. Complete `trace_mark_object` in `vm.c`
  * If the object is `NULL`, or already marked, return immediately without doing anything.
  * Otherwise, mark the object and push it onto the `gray_objects` stack.
2. Complete `trace_blacken_object` in `vm.c`
  * If the object is an `INTEGER`, `FLOAT` or `STRING` do nothing. These don't contain references to other objects.
  * If it's a `VECTOR3`, call `trace_mark_object` on the `x`, `y`, and `z` fields
  * If it's an `ARRAY`, call `trace_mark_object` on each element.
3. Complete `trace` in `vm.c`
  * Create a `stack_new` with a capacity of `8` called `gray_objects`. If it fails, `return`
  * Iterate over each of the objects in the VM: If the object is marked, push it onto the `gray_objects` stack
  * While the `gray_objects` stack is not empty:
    1. Pop an object off the `gray_objects` stack
    2. Call `trace_blacken_object` on the object
4. `stack_free(gray_objects)`

```C
// End of lesson vm.c
#include "vm.h"
#include "stack.h"

void trace(vm_t *vm) {
  stack_t *gray_objects = stack_new(8);
  if (gray_objects == NULL) {
    return;
  }

  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_t *obj = vm->objects->data[i];
    if (obj->is_marked) {
      stack_push(gray_objects, obj);
    }
  }

  while (gray_objects->count > 0) {
    void *top = stack_pop(gray_objects);
    trace_blacken_object(gray_objects, top);
  }

  stack_free(gray_objects);
}

void trace_blacken_object(stack_t *gray_objects, snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
  case STRING:
    break;
  case VECTOR3: {
    snek_vector_t vec = obj->data.v_vector3;
    trace_mark_object(gray_objects, vec.x);
    trace_mark_object(gray_objects, vec.y);
    trace_mark_object(gray_objects, vec.z);
    break;
  }
  case ARRAY: {
    for (size_t i = 0; i < obj->data.v_array.size; i++) {
      trace_mark_object(gray_objects, obj->data.v_array.elements[i]);
    }
    break;
  }
  }
}

void trace_mark_object(stack_t *gray_objects, snek_object_t *obj) {
  if (obj == NULL || obj->is_marked) {
    return;
  }

  stack_push(gray_objects, obj);
  obj->is_marked = true;
}

// don't touch below this line

void mark(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_t *frame = vm->frames->data[i];
    for (size_t j = 0; j < frame->references->count; j++) {
      snek_object_t *obj = frame->references->data[j];
      obj->is_marked = true;
    }
  }
}

void frame_reference_object(frame_t *frame, snek_object_t *obj) {
  stack_push(frame->references, obj);
}

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
  // Free the stack frames, and then their container
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);

  // Free the objects, and then their container
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_free(vm->objects->data[i]);
  }
  stack_free(vm->objects);

  free(vm);
}

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

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}
```
# Sweep

Sweep is easy! Trace was probably the hardest part of the garbage collector.

Every object now has an `is_marked` field that we can use to determine if an object is reachable or not. All we need to do is iterate over all the objects in the VM and free any object that is not marked. Once it's freed, we can also remove it from our VM.
> [!NOTE]
> _**One thing that's not obvious about**_ `sweep()`: _**Any object that is marked (we don't want to free it right now) needs to be reset to**_ `is_marked = false`**. _That way the next time the mark phase runs, if it's_ not marked again _it will be freed in the next cycle._**

### Assignment

1. Complete the `sweep` function
  * Iterate over all of the VM objects
      1. If the object is marked, reset `is_marked = false` and continue
      2. Otherwise free the object and set the data at the position in the stack to `NULL`
  * Call `stack_remove_nulls` to remove any `NULL` objects from the VM's object stack.
2. Complete the `vm_collect_garbage` function.
  * Call `mark`
  * Call `trace`
  * Call `sweep`
```C
// End of lesson vm.c
#include "vm.h"
#include "snekobject.h"
#include "stack.h"

void vm_collect_garbage(vm_t *vm) {
  mark(vm);
  trace(vm);
  sweep(vm);
}

void sweep(vm_t *vm) {
  for (int i = 0; i < vm->objects->count; i++) {
    snek_object_t *obj = vm->objects->data[i];
    if (obj->is_marked) {
      obj->is_marked = false;
    } else {
      snek_object_free(obj);
      vm->objects->data[i] = NULL;
    }
  }

  stack_remove_nulls(vm->objects);
}

// don't touch below this line

void mark(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_t *frame = vm->frames->data[i];
    for (size_t j = 0; j < frame->references->count; j++) {
      snek_object_t *obj = frame->references->data[j];
      obj->is_marked = true;
    }
  }
}

void trace(vm_t *vm) {
  stack_t *gray_objects = stack_new(8);
  if (gray_objects == NULL) {
    return;
  }

  // Get previously marked objects (which are the roots)
  for (int i = 0; i < vm->objects->count; i++) {
    snek_object_t *obj = vm->objects->data[i];
    if (obj->is_marked) {
      stack_push(gray_objects, obj);
    }
  }

  // Trace through the objects
  while (gray_objects->count > 0) {
    trace_blacken_object(gray_objects, stack_pop(gray_objects));
  }

  // Clean up after ourselves :)
  stack_free(gray_objects);
}

void trace_blacken_object(stack_t *gray_objects, snek_object_t *ref) {
  snek_object_t *obj = ref;

  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
  case STRING:
    break;
  case VECTOR3: {
    snek_vector_t vec = obj->data.v_vector3;
    trace_mark_object(gray_objects, vec.x);
    trace_mark_object(gray_objects, vec.y);
    trace_mark_object(gray_objects, vec.z);
    break;
  }
  case ARRAY: {
    for (size_t i = 0; i < obj->data.v_array.size; i++) {
      trace_mark_object(gray_objects, obj->data.v_array.elements[i]);
    }
    break;
  }
  }
}

void trace_mark_object(stack_t *gray_objects, snek_object_t *obj) {
  if (obj == NULL || obj->is_marked) {
    return;
  }

  stack_push(gray_objects, obj);
  obj->is_marked = true;
}

void frame_reference_object(frame_t *frame, snek_object_t *obj) {
  stack_push(frame->references, obj);
}

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
  // Free the stack frames, and then their container
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);

  // Free the objects, and then their container
  for (size_t i = 0; i < vm->objects->count; i++) {
    snek_object_free(vm->objects->data[i]);
  }
  stack_free(vm->objects);

  free(vm);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_frame_pop(vm_t *vm) { return stack_pop(vm->frames); }

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

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}

// See last section of CH 11 Mark and Sweep GC Codebase for full code.
```
