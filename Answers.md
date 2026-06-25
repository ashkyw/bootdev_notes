```C
// snekobject.c
#include "snekobject.h"

void snek_object_free(snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    free(obj->data.v_string);
    break;
  case VECTOR3:
    break;
  case ARRAY: 
    free(obj->data.v_array.elements);
    break;
  }
  free(obj);
}

// vm.c
#include "vm.h"
#include "stack.h"

void vm_free(vm_t *vm) {
  for (int i = 0; i < vm->frames->capacity; i++) {
    stack_free(vm->frames);
    for (int j = 0; j < vm->objects->capacity; j++) {
      snek_object_free(vm->objects);
      stack_free(vm->objects);
      free(vm);
    }
  }
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

```
