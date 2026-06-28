Memory Management CH 11 - Lesson 2
```C
// vm.c
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

// main.c
#include "bootlib.h"
#include "munit.h"
#include "vm.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, test_vm_new, {
  vm_t *vm = vm_new();
  assert_int(vm->frames->capacity, ==, 8, "frames should have capacity 8");
  assert_int(vm->objects->capacity, ==, 8, "objects should have capacity 8");
  vm_free(vm);
});

munit_case(SUBMIT, test_vm_new_free, {
  vm_t *vm = vm_new();
  vm_free(vm);
  assert(boot_all_freed());
});

int main() {
  MunitTest tests[] = {
      munit_test("/vm", test_vm_new),
      munit_test("/vm", test_vm_new_free),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("mark-and-sweep", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}

// snekobject.h
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
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

// stack.c
#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    // Double stack capacity to avoid reallocing often
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      // Unable to realloc, just exit :) get gud
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
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

// stack.h
#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

// vm.h
#include "stack.h"

typedef struct VirtualMachine {
  stack_t *frames;
  stack_t *objects;
} vm_t;

vm_t *vm_new();
void vm_free(vm_t *vm);

```
Memory Management CH 11 - Lesson 3
```C
// main.c

#include "bootlib.h"
#include "munit.h"
#include "vm.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, test_vm_new, {
  vm_t *vm = vm_new();
  vm_new_frame(vm);
  assert_int(vm->frames->count, ==, 1, "frame was pushed");
  vm_free(vm);
});

munit_case(RUN, test_vm_new_frame, {
  vm_t *vm = vm_new();
  frame_t *frame = vm_new_frame(vm);
  assert_ptr(frame->references, !=, NULL,
             "frame->references must be allocated");
  assert_int(frame->references->count, ==, 0,
             "references stack should start empty");
  assert(frame->references->capacity >
         0); // references stack must have capacity > 0
  assert_ptr(frame->references->data, !=, NULL,
             "references stack backing array must be allocated");
  vm_free(vm);
});

munit_case(RUN, test_frames_are_freed, {
  vm_t *vm = vm_new();
  vm_new_frame(vm);
  vm_free(vm);
  assert(boot_all_freed());
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_vm_new", test_vm_new),
      munit_test("/test_vm_new_frame", test_vm_new_frame),
      munit_test("/test_frames_are_freed", test_frames_are_freed),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("mark-and-sweep", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}

// snekobject.h

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
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

// stack.c

#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    // Double stack capacity to avoid reallocing often
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      // Unable to realloc, just exit :) get gud
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
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

// stack.h

#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

// vm.h

#include "stack.h"

typedef struct VirtualMachine {
  stack_t *frames;
  stack_t *objects;
} vm_t;

typedef struct StackFrame {
  stack_t *references;
} frame_t;

vm_t *vm_new();
void vm_free(vm_t *vm);

void vm_frame_push(vm_t *vm, frame_t *frame);
frame_t *vm_new_frame(vm_t *vm);

void frame_free(frame_t *frame);

```

Memory Management CH 11 - Lesson 4
```C
// main.c
#include "bootlib.h"
#include "munit.h"
#include "sneknew.h"
#include "snekobject.h"
#include "vm.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, test_new_object, {
  vm_t *vm = vm_new();
  snek_object_t *obj = new_snek_integer(vm, 5);
  assert_int(obj->kind, ==, INTEGER, "kind must be INTEGER");
  assert_ptr_equal(vm->objects->data[0], obj, "object must be tracked");
  free(obj);
  vm_free(vm);
  assert(boot_all_freed());
});

munit_case(RUN, test_vm_new, {
  vm_t *vm = vm_new();
  assert_ptr_not_null(vm->frames, "frames must not be NULL");
  assert_ptr_not_null(vm->objects, "objects must not be NULL");
  vm_free(vm);
  assert(boot_all_freed());
});

munit_case(RUN, test_frames_are_freed, {
  vm_t *vm = vm_new();
  vm_new_frame(vm);
  vm_free(vm);
  assert(boot_all_freed());
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_vm_new", test_vm_new),
      munit_test("/test_frames_are_freed", test_frames_are_freed),
      munit_test("/test_new_object", test_new_object),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("mark-and-sweep", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}

// sneknew.h
#pragma once

#include "snekobject.h"
#include "vm.h"

snek_object_t *new_snek_integer(vm_t *vm, int value);
snek_object_t *new_snek_float(vm_t *vm, float value);
snek_object_t *new_snek_string(vm_t *vm, char *value);
snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(vm_t *vm, size_t size);

// snekobject.h
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
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

// stack.c
#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  assert_ptr_not_null(obj, "must not have null obj");

  if (stack->count == stack->capacity) {
    // Double stack capacity to avoid reallocing often
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      // Unable to realloc, just exit :) get gud
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
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

// stack.h
#pragma once

#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

// vm.h
#pragma once

#include "snekobject.h"
#include "stack.h"

typedef struct VirtualMachine {
  stack_t *frames;
  stack_t *objects;
} vm_t;

typedef struct StackFrame {
  stack_t *references;
} frame_t;

vm_t *vm_new();
void vm_free(vm_t *vm);
void vm_track_object(vm_t *vm, snek_object_t *obj);

void vm_frame_push(vm_t *vm, frame_t *frame);
frame_t *vm_new_frame(vm_t *vm);

void frame_free(frame_t *frame);
```
Memory Management CH 11 - Lesson 5
```C
// main.c
#include "bootlib.h"
#include "munit.h"
#include "sneknew.h"
#include "vm.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, test_reference_object, {
  vm_t *vm = vm_new();
  new_snek_integer(vm, 5);
  new_snek_string(vm, "hello");
  vm_free(vm);
  assert(boot_all_freed());
});

munit_case(RUN, test_array_freed, {
  vm_t *vm = vm_new();
  new_snek_array(vm, 3);
  vm_free(vm);
  assert(boot_all_freed());
});

munit_case(SUBMIT, test_frames_are_freed, {
  vm_t *vm = vm_new();
  vm_new_frame(vm);
  vm_new_frame(vm);
  vm_free(vm);
  assert(boot_all_freed());
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_reference_object", test_reference_object),
      munit_test("/test_array_freed", test_array_freed),
      munit_test("/test_frames_are_freed", test_frames_are_freed),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("mark-and-sweep", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}

// sneknew.c
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

// sneknew.h
#pragma once

#include "snekobject.h"
#include "vm.h"

snek_object_t *new_snek_integer(vm_t *vm, int value);
snek_object_t *new_snek_float(vm_t *vm, float value);
snek_object_t *new_snek_string(vm_t *vm, char *value);
snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(vm_t *vm, size_t size);

// snekobject.h
#pragma once

#include "stack.h"
#include <stdbool.h>
#include <stddef.h>

typedef struct SnekObject snek_object_t;

void snek_object_free(snek_object_t *obj);

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

// stack.c
#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  assert_ptr_not_null(obj, "must not have null obj");

  if (stack->count == stack->capacity) {
    // Double stack capacity to avoid reallocing often
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      // Unable to realloc, just exit :) get gud
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
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

// stack.h
#pragma once

#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

// vm.h
#pragma once

#include "snekobject.h"
#include "stack.h"

typedef struct VirtualMachine {
  stack_t *frames;
  stack_t *objects;
} vm_t;

typedef struct StackFrame {
  stack_t *references;
} frame_t;

vm_t *vm_new();
void vm_free(vm_t *vm);
void vm_track_object(vm_t *vm, snek_object_t *obj);

void vm_frame_push(vm_t *vm, frame_t *frame);
frame_t *vm_new_frame(vm_t *vm);

void frame_free(frame_t *frame);
```
Memory Management CH 11 - Full codebase
```C
// vm.c
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

// sneknew.c

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

// sneknew.h

#pragma once

#include "snekobject.h"
#include "vm.h"

snek_object_t *new_snek_integer(vm_t *vm, int value);
snek_object_t *new_snek_float(vm_t *vm, float value);
snek_object_t *new_snek_string(vm_t *vm, char *value);
snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(vm_t *vm, size_t size);

// snekobject.c

#include "snekobject.h"
#include "sneknew.h"
#include <string.h>

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

  // Get the value directly now (already checked size constraint)
  return array->data.v_array.elements[index];
}

snek_object_t *snek_add(vm_t *vm, snek_object_t *a, snek_object_t *b) {
  if (a == NULL || b == NULL) {
    return NULL;
  }

  switch (a->kind) {
  case INTEGER:
    switch (b->kind) {
    case INTEGER:
      return new_snek_integer(vm, a->data.v_int + b->data.v_int);
    case FLOAT:
      return new_snek_float(vm, (float)a->data.v_int + b->data.v_float);
    default:
      return NULL;
    }
  case FLOAT:
    switch (b->kind) {
    case FLOAT:
      return new_snek_float(vm, a->data.v_float + b->data.v_float);
    default:
      return snek_add(vm, b, a);
    }
  case STRING:
    switch (b->kind) {
    case STRING: {
      int a_len = strlen(a->data.v_string);
      int b_len = strlen(b->data.v_string);
      int len = a_len + b_len + 1;
      char *dst = malloc(len * sizeof(char));
      dst[0] = '\0';

      strcat(dst, a->data.v_string);
      strcat(dst, b->data.v_string);

      snek_object_t *obj = new_snek_string(vm, dst);
      free(dst);

      return obj;
    }
    default:
      return NULL;
    }
  case VECTOR3:
    switch (b->kind) {
    case VECTOR3:
      return new_snek_vector3(
          vm, snek_add(vm, a->data.v_vector3.x, b->data.v_vector3.x),
          snek_add(vm, a->data.v_vector3.y, b->data.v_vector3.y),
          snek_add(vm, a->data.v_vector3.z, b->data.v_vector3.z));
    default:
      return NULL;
    }
  case ARRAY:
    switch (b->kind) {
    case ARRAY: {
      size_t a_len = a->data.v_array.size;
      size_t b_len = b->data.v_array.size;
      size_t length = a_len + b_len;

      snek_object_t *array = new_snek_array(vm, length);

      for (int i = 0; i < a_len; i++) {
        snek_array_set(array, i, snek_array_get(a, i));
      }

      for (int i = 0; i < b_len; i++) {
        snek_array_set(array, i + a_len, snek_array_get(b, i));
      }

      return array;
    }
    default:
      return NULL;
    }
  default:
    return NULL;
  }
}

// snekobject.h

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

bool snek_array_set(snek_object_t *array, size_t index, snek_object_t *value);
snek_object_t *snek_array_get(snek_object_t *array, size_t index);

// stack.c

#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
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

// stack.h

#pragma once

#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

// vm.h

#pragma once

#include "snekobject.h"
#include "stack.h"

typedef struct VirtualMachine {
  // stack frames: stack_t frame_t
  stack_t *frames;

  // These are the rest of the objects: stack_t snek_object_t
  stack_t *objects;
} vm_t;

typedef struct StackFrame {
  stack_t *references;
} frame_t;

/// Our main functions for garbage collection.
void mark(vm_t *vm);
void trace(vm_t *vm);
void sweep(vm_t *vm);

void vm_collect_garbage(vm_t *vm);

/// Helper functions for `trace`
void trace_blacken_object(stack_t *gray_objects, snek_object_t *ref);
void trace_mark_object(stack_t *gray_objects, snek_object_t *ref);

/// This is the function that gets called to actually do the garbage collection,
/// but is just composed of `mark`, `trace`, and `sweep`.
///
/// Don't worry, it's not going to delete your code (hopefully!)
void vm_collect_garbage(vm_t *vm);

/// Already implemented
vm_t *vm_new();
void vm_free(vm_t *vm);
void vm_track_object(vm_t *vm, snek_object_t *obj);

frame_t *vm_new_frame(vm_t *vm);
void vm_frame_push(vm_t *vm, frame_t *frame);
frame_t *vm_frame_pop(vm_t *vm);

void frame_free(frame_t *frame);

// Marks the object as referenced in the current stack frame.
void frame_reference_object(frame_t *frame, snek_object_t *obj);
```
