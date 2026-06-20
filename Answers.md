```C
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *snek_add(snek_object_t *a, snek_object_t *b) {
  if (a == NULL || b == NULL) {
    return NULL;
  }
  switch (a->kind) {
    case INTEGER:
      if (b->kind == INTEGER) {
        int sum = a->data.v_int + b->data.v_int;
        return new_snek_integer(sum);
      } else if (b->kind == FLOAT) {
        float sum = a->data.v_int + b->data.v_int;
        return new_snek_float(sum);
      } else {
        return NULL;
      }
    case FLOAT:
      if (b->kind == INTEGER) {
        float sum = a->data.v_float + b->data.v_int;
        return new_snek_float(sum);
      } else if (b->kind == FLOAT) {
        float sum = a->data.v_float + b->data.v_float;
        return new_snek_float(sum);
      } else {
        return NULL;
      }
    case STRING:
      if (b->kind != STRING) {
        return NULL;
      } else {
        int a_len = strlen(a->data.v_string) + 1;
        int b_len = strlen(b->data.v_string) + 1;
        int total_len = (a_len + b_len);
        char *new_str = calloc(2, total_len);
        if (new_str == NULL) {
          return NULL;
        } 
        new_str = strcat(new_str, a->data.v_string);
        new_str = strcat(new_str, b->data.v_string);
        snek_object_t *temp_str = new_snek_string(new_str);
        free(new_str);
        return temp_str;
      }
    case VECTOR3:
      if (b->kind != VECTOR3) {
        return NULL;
      } else {
        return "TODO";
        // snek_object_t *sum_vector = new_snek_vector3(b->data.v_vector3.x, b->data.v_vector3.y, b->data.v_vector3.z);
        // for (int i = 0; i++ i < (snek_length(b) + 1)) {
          // snek_add(a->data.v_vector3) 
        }
      }
    case ARRAY:
      if (b->kind != ARRAY){
        return NULL;
      }
      return "TODO";
    default:
      return NULL;
  }
}

// don't touch below this line

int snek_length(snek_object_t *obj) {
  if (obj == NULL) {
    return -1;
  }

  switch (obj->kind) {
  case INTEGER:
    return 1;
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
```
