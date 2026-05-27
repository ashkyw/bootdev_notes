# Structs

##### [Video notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/what-are-structs-1920x1080.mp4)

Structs in C are similar to objects & classes in other languages, but simpler. There's no concepts of inheritance, class methods, or static variables.
Instead, they are simply a way to group multiple fields or data points and put them all into one _object_. This way they can be moved around and stored together.

Instead of typing numerous variables for a function, we can logically group them into a struct and pass them around together. 
Much like how classes in Python group things together. 

Structs do not have any behavior, they are simply just data.

Struct fields can be accessed with the `.` operator. If you have a pointer, it can be accessed with the `->` operator.

One difference between structs and classes is that the declaration order matters. This determines the size and layout of memory for the struct.

When we make a struct what we're doing is telling C that we have several different pieces of data that we want grouped together in memory, so we can operate on that memory as a block. That block can be bigger or smaller depending on how we lay out the data.

##### Lesson Notes

So far all we've seen are the _simple_ (non-collection) types in C. However, stuff like this can get really annoying:
```C
int main() {
    int x_1 = 1;
    int y_1 = 2;
    int z_1 = 3;
    int x_2 = 4;
    int y_2 = 5;
    int z_2 = 6;

    int dist = distance(x_1, y_1, z_1, x_2, y_2, z_2);
    printf("Distance: %d", dist);
}
```
Because our distance function starts to look... ridiculous.
```C
int distance(int x_1, int y_1, int z_1,
             int x_2, int y_2, int z_2)
{
    // a lot of numbers
}
```
We also run into a new problem: _In C, we're only allowed to return a single value from a function_. This doesn't work:

```C
int int int scale_coordinate(int x, int y, int z, int scale) {
    return x * scale, y * scale, z * scale;
    // Error! Too many values to return
}
```
_[Structs](https://en.cppreference.com/w/c/language/struct) solve this_. Here's an example of the syntax:
```C
struct Human {
    int age;
    char *name;
    int is_alive;
};
```

```C
// End of lesson code

#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};
```

# Initializers

So now you're probably wondering: "How do we actually _make an instance of_ a struct"? You may have noticed in the previous lesson all we did was _define the struct type_.

Unfortunately, there are a few different ways to [initialize a struct](https://en.cppreference.com/w/c/language/struct_initialization). The following examples will be using this struct.

```C
struct City {
  char *name;
  int lat;
  int lon;
};
```
### Zero Initializer
```C
int main() {
  struct City c = {0};
}
```
This sets all the fields to `0` values.

### Positional Initializer

```C
int main() {
  struct City c = {"San Francisco", 37, -122};
}
```

### Designated Initializer

This is generally the preferred way to initialize a struct.

  * It's easier to read (has the field names)
  * If the fields change, you don't have to worry about breaking the ordering
```C
int main() {
  struct City c = {
    .name = "San Francisco",
    .lat = 37,
    .lon = -122
  };
}
```

Remember, it's `.name` not `name`. If this trips you up, just remember it's `.name` and not `name` because that's how you access the field, e.g. `c.name`.

## Accessing Fields

Accessing a field in a struct is done using the `.` operator. For example:

```C
struct City c;
c.lat = 41; // Set the latitude
printf("Latitude: %d", c.lat); // Print the latitude
```

```C
// End of lesson code

#include "coord.h"

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};
  return coord;
}
```

### Scaling Coordinate

Remember how we can **not** return multiple values from a function in C? We can't do this:
```C
int, char * become_older(int age, char *name) {
    return age + 1, name;
}
```
However, we _can_ accomplish effectively the same thing by returning a `struct`:

```C
struct Human become_older(int age, char *name) {
    struct Human h = {.age = age, .name = name};
    h.age++;
    return h;
}
```
```C
// End of lesson code .c file
#include "coord.h"

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};
  return coord;
}

struct Coordinate scale_coordinate(struct Coordinate coord, int factor) {
  struct Coordinate scaled = coord;
  scaled.x *= factor;
  scaled.y *= factor;
  scaled.z *= factor;
  return scaled;
}

// End of lesson code .h file
#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};

struct Coordinate new_coord(int x, int y, int z);
struct Coordinate scale_coordinate(struct Coordinate coord, int factor);

```
# Typedef

By now, you're probably tired of typine `struct Coordinate` over and over again, and wondering, "How can I make my struct types easier to write, like `int`?"

Good news, everyone! C can do this with the [`typedef keyword`](https://en.cppreference.com/w/c/language/typedef).

```C
struct Pastry {
    char *name;
    float weight;
}
```
Can also be written as:
```C
typedef struct Pastry {
    char *name;
    float weight;
} pastry_t; 
```
Now we can use `pastry_t` wherever we would have used `struct Pastry` before.

> [!Information]
> The `_t` at the end is a common convention to indicate a type.

In fact, you can optionally skip giving the struct a name:

```C
typedef struct{
    char *name;
    float weight;
} pastry_t;

pastry_t muffin = {"Muffin", 0.3};
```
In this case you'd only be able te refer to the type as `pastry_t`. In general, give the struct an actual name (e.g. `Pastry`).
```C
// End of lesson .c file
#include "coord.h"


coordinate_t new_coord(int x, int y, int z) {
  coordinate_t coord = {.x = x, .y = y, .z = z};

  return coord;
}

coordinate_t scale_coordinate(coordinate_t coord, int factor) {
  coordinate_t scaled = coord;
  scaled.x *= factor;
  scaled.y *= factor;
  scaled.z *= factor;

  return scaled;
}

// End of lesson .h file
#pragma once

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

coordinate_t new_coord(int x, int y, int z);
coordinate_t scale_coordinate(coordinate_t, int factor);
```

# Sizeof

As we saw earlier, [sizeof]() can be used to view the size of a type (for once, programmers thought of a name that was actually helpful!) But this isn't just true of builtin types like `int` or `float`, it can also be used to find out the size of `struct`s!

```C
printf("Size of coordinate_t: %zu bytes\n", sizeof(coordinate_t));
```
## Memory Layout

Structs are stored contiguously in memory one field after another. Take this struct:
```C
typedef struct Coordinate {
    int x;
    int y;
    int z;
} coordinate_t;
```
Assuming `int` is 4 bytes, the memory layout for `coordinate_t` would look like:

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Coordinate%20Struct.png)

## Mixed Type Structs
```C
typedef struct Human {
    char first_intial;
    int age;
    double height;
} human_t;
```
Assuming `char` is 1 byte, `int` is 4 bytes, and `double` is 8 bytes, the memory layout for `human_t` might look like this:

![Alt text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Human%20Struct.png)

Wait! What is that `padding` doing there?

It turns out, CPUs don't like accessing data that isn't [aligne](https://en.wikipedia.org/wiki/Data_structure_alignment) (this is a radical oversimplification), so C inserts padding to maintain alignment (e.g. every 4 bytes in this example).

_**HUGE CAVEAT:** these layouts can vary depending on the compiler and system architecture._

# Struct Padding

There are a bunch of complicated rules and heuristics that different compilers use to determine how to lay out your structs. But to oversimppify:

  1. The structs are laid out in memory contiguously.
  2. Structs can vary in size depending on how they are laid out.

C is a language that aims to give tight control over memory, so the fact that you can control the layout of your structs is a _feature_, not a bug.

Compilers + modern hardware + optimizations + skill issues means that sometimes what you _think_ the computer is going to do isn't exactly what it actually _does_. That said, C is designed to get you close to the machine and allows you to dig in and figure out what's going on if you want to for a specific compiler or architecture. 

As a _rule of thumb_, ordering your fields from largest to smallest will help the compiler minimize padding:
```C
typedef struct {
    char* a;
    double b;
    char c;
    char d;
    long e;
    char f;
} poorly_aligned_t;

typedef struct {
    double b;
    long e;
    char* a;
    char c;
    char d;
    char f;
} better_t;
```
```C
// End of lesson .h
#pragma once

typedef struct SneklangVar {
  double weight;
  char *name;
  int scope_level;
  int value;
  char type;
  char is_constant;
} sneklang_var_t;

```
