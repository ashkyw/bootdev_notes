# Garbage Collector

## [Video Notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/garbage-collection-1920x1080.mp4)

There are different kinds of garbage collectors.
#### Reference Counting
Possibly the simplest version. With this, it adds an additional field to each object that is it's count
```C
typedef struct Object {
  object_kind_t kind;
  object_kind_t data;
  object_kind_t refcount;
} object_t;
```
With this, every time an object is created or referenced the refcount increments.
```py
foo = 42 #refcount: 1
list = [foo] #refcount: 2
pop(list(foo)) #refcount: 1
```
If an object is no longer in use, the refcount decrements. Once the refcount is `0`, that memory is returned to the OS.

Reference Counting lacks the ability to track cycles. It's also expensive because everytime we do an operation, we need to modify all other objects it touches. Once that's done, we can then determine everything that is directly referenced and indirectly referenced. Any variables that aren't marked can then return that memory to the OS. 

#### Mark and Sweep
The idea that we can find all of the variable that are directly referenced by our stack frames. Then we trace through all of connections that are referenced by their roots. Any thing not referenced can be returned to the OS.

This is more complex. But it can handle cases that just reference counting can't, like a list that references another list, that references back to the original list (this is known as a cycle). 

Mark and sweep doesn't require us to do operations _every single time_ we touch or reference a variable. Work only needs to be done when we perform a "GC Pause" (garbage collector pause) which is when the GC goes and checks which variables are still alive.

## Lesson notes

A garbage collector is a program (or part of a program) that automatically frees memory thet is no longer in use. Languages like Python, Java, Javascript, OCaml, and even Go use garbage collectors _as the code is running_ to manage memory.
It's "automatic memory management." Automatic memory management can be a huge productivity boost for devs (less code, possibli fewer memory-related bugs) but it typically comes with a performance cost because the garbage collector is always running.
It's not coincedence that C, C++, Rust and Zig are all great choices when you need to squeeze every last drop of performance.

Ultimately, there is a cost with memory, the question is where do you want to pay it? In dev time, or runtime?

# Refcounting

One of the simplest ways to implement a garbage collector is to use a [reference counting](https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)#Reference_counting) algorithm. It goes something like this:
  
  * All objects keep track of a `reference_count` integer.
  * When that object is referenced, its reference count is incremented.
  * When an object is garbage collected, the reference count of any object it references is decremented.
  * When any object's reference count reaches zero, the object is garbage collected.

### Assignment
1. `snekobject.h` add new integer field`refcount` to `snek_object_t`
2. `snekobject.c` complete the `_new_snek_object` functon
    * Allocate a `snek_object_t` on the heap using `calloc` so its memory is zero-initialized
    * if allocation fails return `NULL`
    * Set `refcount` to `1`
    * Return pointer

```C
// End of lesson .c file
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object() {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->refcount = 1;

  return obj;
}

// don't touch below this line

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = _new_snek_object();
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

  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = _new_snek_object();
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
  int refcount;
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

# Increment

We need to be able to increment the reference count of a `SnekObject` any time a reference to it is created

### Assignment

Complete the `refcount_inc` function. It should increment the `refcount` of a `SnekObject`. If the object is `NULL`, it should safely do nothing.

```C
// End of lesson .c file
#include "snekobject.h"
#include "assert.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void refcount_inc(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount++;
}

// don't touch below this line

snek_object_t *_new_snek_object() {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->refcount = 1;

  return obj;
}

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = _new_snek_object();
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

  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = _new_snek_object();
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
// No changes from previous lesson
```

# Decrement and free
Now things are going to get a touch more complicated. In a refcounting GC, the interesting stuff happens when the refcount equals `0`. That's when the garbage gets collected.

When the refcount reaches zero there are no references to this object anymore. So we need to `free` the memory.

For our first pass, we'll only handel ints, floats and strings. It will get harder.

### Assignment
1. `refcount_dec`
    * Handle `NULL` objects
    * Decrement `refcount`
    * `if refcount == 0` call `refcount_free` on object
3. `refcount_free`
    * If `INTEGER` or `FLOAT`, free the object itself, we don't need to worry about the data inside the object because it's stored directly in the object
    * If the object is `STRING`, free the `char *` inside the object, then free the object itself.
    * If any other type, do nothing.

```C
// End of lesson .c file

// End of lesson .h file
// No changes
```

## Notes from boots AI

### Assignment

##
