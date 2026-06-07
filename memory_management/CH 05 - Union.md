# Union

Now that we understand `struct` and `enum`, we can learn about `union`; a combination of the two concepts.

Unions in C can hold one of several types. They're like a less-strict [sum type](https://en.wikipedia.org/wiki/Algebraic_data_type) from the world of functional programming. Here's an example union:
```C
typedef union AgeOrName {
  int age;
  char *name;
} age_or_name_t
```
The `age_or_name_t` type can hold _either_ an `int` or `char *`, but not both at the same time (that would be a struct). We provide the list of possible types so that the C compiler knows the _maximum_ potential memory requirement, and can account for that. This is how the union is used:
```C
age_or_name_t lane = {.age = 29};
printf("age: %d\n", lane.age);
// age: 29
```
Here's where it gets interesting. What happens if we try to access the `name` field (even though we _set_ the `age` field)?
```C
printf("name: %s\n", lane.name);
// name:
```
We get...nothing? To be more specific, we get undefined behavior. A `union` only reserves enough space to hold the largest type in the union and the _all_ of the fields **use the same memory**. So when we set `.age` to 29, we are writing the integer representation of `29` to the memory of the `lane` union:
```C
0000 0000 0000 0000 0000 0000 0001 1101
```
Then we try to access `.name`, we read from the **same block of memory** but try to interpret the bytes as `char *`, which is why we get garbage (which is interpreted as nothing in this case). Put simply, setting the value of `.age` overwrites the value of `.name` and vice versa, and you should only access the field that you set.
```C
// End of lesson .c file
#include "exercise.h"
#include <stdio.h>

void format_object(snek_object_t obj, char *buffer) {
  switch (obj.kind) {
  case INTEGER:
    sprintf(buffer, "int:%d", obj.data.v_int);
    break;
  case STRING:
    sprintf(buffer, "string:%s", obj.data.v_string);
    break;
  }
}

// don't touch below this line

snek_object_t new_integer(int i) {
  return (snek_object_t){
      .kind = INTEGER,
      .data = {.v_int = i},
  };
}

snek_object_t new_string(char *str) {
  // NOTE: We will learn how to copy this data later.
  return (snek_object_t){
      .kind = STRING,
      .data = {.v_string = str},
  };
}

// End of lesson .h file
typedef enum SnekObjectKind {
  INTEGER,
  STRING,
} snek_object_kind_t;

// don't touch below this line

typedef union SnekObjectData {
  int v_int;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t new_integer(int);
snek_object_t new_string(char *str);
void format_object(snek_object_t obj, char *buffer);
```
# Memory Layout

Unions store their value in the same memory location, no matter which field or type is actively being used. That means accessing any field apart from the one you set is generally a **bad idea**.

# Union Size

A downside of unions is that the size of the union is the size of the _largest_ field in the union. Take this example:
```C
typedef union IntOrErrMessaga {
  int data;
  char err[256];
} int_or_err_meassage_t;
```
This `IntOrErrMessage` union is designed to hold an `int` 99% of the time. However, when the program encounters an error, instead of storing an integer here, it will store an error message. The trouble is that it's incredibly inefficient because it allocates 256 bytes for every `int` it stores!

Imagine an array of 1000 `int_or_err_message_t` objects. Even if none of them make use of the `.err` field, the array will take up `256 * 1000 = 256,000` bytes of memory! An array of `int`s would have only taken `4,000` bytes (assuming 32-bit integers).

# Helper Fields

One interesting (albeit not commonly used) trick is to use unions to create "helpers" for accessing different parts of a piece of memory. Consider the following:
```C
typedef union Color {
  struct {
    uint8_t r;
    uint8_t g;
    uint8_t b;
    uint8_t a;
  } components;
  unit32_t rgba;
} color_t;
```
It results in a memory layout like this: 
(!Struct nested in Union memory layout)[https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Struct%20nested%20in%20a%20union.png]
Only 4 bytes are used. And, unlike in 99% of scenarios, it makes sense to both set _and_ get values from this union through both the `components` and `rgba` fields! Both fields in the union are exactly 32 bits in size, which means that we can "safely" (?) access the entire set of colors through the `.rgba` field, or get a single color component through the `.components` field.

The convenience of additional fields, with the efficiency of a single memory location!
```C
// End of lesson code

```
