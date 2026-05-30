# Memory

Some mental models to think about variables in memory:

> Variables are human readable names that refer to some data in memory

> Memory is a big array of bytes, and data is stored in the array.

A variable is a human readable name that refers to an address in memory, which is an index into the big array of bytes. Here's a diagram:

![Alt Text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Memory%20-%20Variables.png)

## Getting a Variable's Address

In C, you can print the address of a variable by using the address-of-operator: `&`. Here's an example:

```C
#include <stdio.h>

int main() {
  int age = 37;
  printf("The address of age is: %p\n", &age);
  return 0;
}

// The address of age is: 0xfff8
```

> [!Note]
> The [`%p` format specifier](https://en.cppreference.com/w/c/io/fprintf#:~:text=The%20following%20format%20specifiers%20are%20available%3A) will format a pointer (memory address) to be printed.

```C
// End of lesson .c file

#include "snek.h"

unsigned long size_of_addr(long long i) {
  unsigned long sizeof_snek_version = sizeof(&i);
  return sizeof_snek_version;
}

// End of lesson .h file

unsigned long size_of_addr(long long i);
```

#  Virtual Memory

As it turns out, code doesn't have direct access to the physical RAM in your computer. 

Instead, the OS provides a layer of abstraction called **virtual memory**. Virtual memory makes it seem like your program has direct access to all the memory on the machine, even if it doesn't.

* **Physical Memory**: The actual RAM sticks in your PC.
* **Operating Sysetm**: The software that manages access te the physical memory.
* **Your Program**: When it runs, it becomes a [`process`](https://en.wikipedia.org/wiki/Process_(computing)) and is given access to a chunk of virtual memory by the OS.
* **Virutal Memory**: This abstracted chunk of memory that your program can use.

  _There are exceptions to this. For example, if you're using C to build embedded firmware that runs without an OS, your code might interact directly with physical memory_.

  ![Alt Text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Memory%20-%20Virtual.png)

By only giving processes access to a chunk of virtual memory, the operating system can do some cool things:
  1. **Isolation**: One process can't access the memory of another process.
  2. **Security**: The OS can prevent processes from accessing certain parts of memory.
  3. **Simplicity**: Developers don't have to worry about managing physical memory of other processes.
  4. **Performance**: The OS can optimize memory access depending on the hardware and needs of the program. For example, by moving data between physical memory and the hard drive.

At the end of the day, your program has direct access to a virtual chunk of memory. Just like physical memory, it can be thought of as a big array of bytes, where each byte has an address.

# Pointers

##### Lesson notes

Put simply: **a pointer is just a variable that stores a memory address**. It's called a pointer because it "points" to the address of a variable, which stores the actual data held in that variable.

## Syntax

A pointer is declared with an asterisk (`*`) after the type. For example, `int *`.
```C
int age = 37;
int *pointer_to_age = &age;
```
We use the address-of-operator `&` to get the address of a variable so it can be stored _in_ a pointer variable.

##### [Pointers Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/pointers-are-easy-1920x1080.mp4) notes

Ultimately, pointers are just a value that tells you the memory address of another value. 

We start with:
```C
int x = 5;
```
| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 5 |

We create another value:
```C
int y = x;
```
Setting one value = to another is a copy operation. So whatever `x` was, is now in `y`. In other words, `y = 5`

| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 5 |
| y | 0x8DAC344 | 5 |

Now, if we update the value of x:
```C
int x = 7;
```
`y = 5` stays true. Only now `x = 7`

| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 7 |
| y | 0x8DAC344 | 5 |

Using pointer syntax:
```C
int *x_ptr = &x;
```
This sets the `x_ptr` variable to the value of the actual **address** of `x`, not the _value_ of `x`

| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 7 |
| y | 0x8DAC344 | 5 |
| x_ptr | 0x3ABF678 | 0x6ABD670 |

So now we dereference the pointer:
```C
int z = *x_ptr;
```
And instead of copying the value from `x`, we instead copy the value stored in the memory address of `x` and set it to `z`

| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 7 |
| y | 0x8DAC344 | 5 |
| x_ptr | 0x3ABF678 | 0x6ABD670 |
| z | 0x20BC112 | 7 |

Now we let's say we want to change what's in the memory location that the pointer points to:

```C
*x_ptr = 12;
```
| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 7 |
| y | 0x8DAC344 | 5 |
| x_ptr | 0x3ABF678 | 0x6ABD670 |
| z | 0x20BC112 | 7 |
| x_ptr | 0x3ABF78 | 0x6ABD670|

And we say we need to update the value of `x`. Because the value of `x_ptr` is simply the memory address of `x`,
we actually end up changing `x` by updating the value of it's current memory address.

| Name | Address | Value |
|:----:|:-------:|:-----:|
| x | 0x6ABD670 | 12 |
| y | 0x8DAC344 | 5 |
| x_ptr | 0x3ABF678 | 0x6ABD670 |
| z | 0x20BC112 | 7 |
| x_ptr | 0x3ABF78 | 0x6ABD670|

# Why Pointers?

To illustrate the usefulness of pointers, let's pretend we want to pass a collection of data into a function. Within that function, we want to modify the data. In Python we could use a class to store the data, and pass an instance of that class into the function:

```py
class Coordinate:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def update_coordinate_x(coord, new_x):
    coord.x = new_x

c = Coordinate(1, 2, 3)
print(c.x) # 1
c = Coordinate(c, 4)
print(c.x) # 4
```

Now, let's do the same thing, but using structs in C.

```C
// End of lesson .c file
#include "coordinate.h"

void coordinate_update_x(coordinate_t coord, int new_x) { coord.x = new_x; }

coordinate_t coordinate_update_and_return_x(coordinate_t coord, int new_x) {
  coord.x = new_x;
  return coord;
}

// End of lesson .h file

typedef struct coordinate {
  int x;
  int y;
  int z;
} coordinate_t;

void coordinate_update_x(coordinate_t coord, int new_x);
coordinate_t coordinate_update_and_return_x(coordinate_t coord, int new_x);

// End of lesson main.c
// Only included to frame the sneakiness of structs
#include "coordinate.h"
#include "munit.h"

coordinate_t new_coordinate(int x, int y, int z) {
  return (coordinate_t){.x = x, .y = y, .z = z};
}

munit_case(RUN, test_unchanged, {
  coordinate_t old = new_coordinate(1, 2, 3);
  munit_assert_int(old.x, ==, 1, "old.x must be 1");

  coordinate_update_x(old, 4);
  munit_assert_int(old.x, ==, 1, "old.x must still be 1");
});

munit_case(SUBMIT, test_changed, {
  coordinate_t old = new_coordinate(1, 2, 3);
  munit_assert_int(old.x, ==, 1, ".x must be 1");

  coordinate_t new = coordinate_update_and_return_x(old, 4);
  munit_assert_int(new.x, ==, 4, "new .x must be 4");
  munit_assert_int(old.x, ==, 1, "old.x must still be 1");

  // Notice, they have different addresses
  munit_assert_ptr_not_equal(&old, &new, "Must be different addresses");
});

int main() {
  MunitTest tests[] = {
      munit_test("/test_unchanged", test_unchanged),
      munit_test("/test_changed", test_changed),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("pointers", tests);

  return munit_suite_main(&suite, NULL, 0, NULL);
}

```
>[!NOTE]
> In C, structs are passed by _value_. That's why updating a field in the struct does _not_ change the original struct from the `main` function.
> To get the change to "persist", we needed to return the updated struct from the function (a new copy).
> The memory address of the struct that went _in_ to `coordinate_update_and_retur_x` was not the same as the address of the struct that was returned. Again, because we created a copy.

# Pointer Basics

Remember, pointers are just an address (read: value) that tells the computer where to look for _other_ values. Just like how the address to your house is not actually your house, but points you to where your house is.

## Syntax Review

Declare a pointer to an integer:

```C
// declares `pointer_to_something` as a pointer to an int
int *pointer_to_something;
```
Get the address of a variable:
```C
int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;
// pointer_to_mol now holds the address of meaning_of_life
```
### Derefencing pointers

Oftentimes we have a pointer, but we want to get access to the data that it points to. Not the address itself, but the value stored at _that_ address. 

We can use an asterisk `*` to do it. The `*` operator dereferences a pointer.
```C
int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;
int value_at_pointer = *pointer_to_mol;
// value_at_pointer = 42
```
It can be confusing. Remember that the asterisk symbol is used for two different things:
  1. Declaring a pointer type: `int *pointer_to_thing;`
  2. Dereferencing a pointer value: `int value = *pointer_to_thing;` (retrieving the value) or `*pointer_to_thing = 20;` (modifying the value)

```C
// End of lesson code .c file
#include "exercise.h"

codefile_t change_filetype(codefile_t *f, int new_filetype) {
  codefile_t new_f = *f;
  new_f.filetype = new_filetype;
  return new_f;
}

// End of lesson code .h file
typedef struct CodeFile {
  int lines;
  int filetype;
} codefile_t;

codefile_t change_filetype(codefile_t *f, int new_filetype);
```

# Pointers to Structs

 When working with a pointer to a struct, you need to use the arrow `->` operator to access a struct's field:

 ```C
coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", ptrToPoint->x); // X: 10
```

It effectively dereferences the pointer and accesses the field in one step. To be fair, you can use the dereference and dot operator (`*` and `.`) to achieve the same result (it's just ugly, more verbose, and less common):

```C
coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", (*ptrToPoint).x); // X: 10
```

## Order of Operations

The `.` operator has a higher precedence than the `*` operator, so parentheses are _**necessary**_ when using `*` to dereference a pointer before accessing a member... which is another reason why the arrow operator is so much more common.

# C Arrays

If you're used to lists in Python, [Arrays in C](https://en.cppreference.com/w/c/language/array) are _similar_, but a bit lower level.

An array is a _fixed-size_, ordered collection of elements. Like Python lists, they are indexed by integers, starting at zero. Unlike Python lists, they can only hold elements of the same type. They are stored in contiguous memory, like structs.

## Integer Array

```C
int numbers[5] = {1, 2, 3, 4, 5};
```

##### Iterating Over an Array

In C, there is no `x for list:`  syntax. Instead, you must iterate over them using a `for` loop with an index (or some conditional loop)

```C
#include <stdio.h>

int main() {
  int numbers[5] = {1, 2, 3, 4, 5};

  // iterate and print each element
  for (int i = 0; i < 5; i++) {
    printf("%d", numbers[i]);
  }
  printf("\n");
  return 0;
}

// Output
1 2 3 4 5
```

##### Updating Values in an Array

The syntax for updating values in an array is the same as how you access them:

`arr[index] = value`

Using our `numbers` example:

```C
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    // Update some values
    numbers[1] = 20;
    numbers[3] = 40;

    // Print updated array
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}

// Output

1 20 3 40 5
```

```C
// End of lesson .c file
#include "exercise.h"

void update_file(int filedata[200], int new_filetype, int new_num_lines) {
  filedata[1] = new_num_lines;
  filedata[2] = new_filetype;
  filedata[199] = 0;
}

// End of lesson .h file
void update_file(int filedata[200], int new_filetype, int new_num_lines);
```

# Arrays As Pointers in C

In C, arrays and pointers are closely related. An array name acts as a pointer to the first element of the array. That means array indexing and pointer arithmetic can be used interchaneably to access array elements. Let's go through this step-by-step to understand how this works.

### Step-by-Step walkthrough

1. **Array Declarations**:
```C
int numbers[5] = {1, 2, 3, 4, 5};
```
  Here `numbers` is an array of 5 integers.
  
2. **Array as Pointer**:
  The name `numbers` acts as a pointer to the first element of the array.
```C
int *numbers_ptr = numbers;
```

3. **Accessing Elements via Indexing**:
```C
// Access index 2
int value = numbers[2];
```

  Which is the same as:

```C
int value = *(numbers + 2);
```
  Here, `numbers + 2` computes the address of the third element and `*` dereferences it to get the value

4. **Pointer Arithmetic**:
  When you add an integer to a pointer, the resulting pointer is offset by that integer times the size of the data type.
```C
int *p = numbers + 2; // p points to the third element
int value = *p; // value is 3
```

###  Diagram Explanation
Let's assume `numbers` is stored starting at memory address `0x1000`. An integer is typically 4 bytes in C. Here's how the array elements are laid out in memory:

| Address | Element | Value |
|:----:|:-------:|:-----:|
| 0x1000 | numbers[0] | 1 |
| 0x1004 | numbers[1] | 2 |
| 0x1008 | numbers[2] | 3 |
| 0x100C | numbers[3] | 4 |
| 0x1010 | numbers[4] | 5 |

### Accessing Elements Using Pointers

* `numbers + 0` or `&numbers[0]` points to `0x1000`
* `numbers + 1` or `&numbers[1]` points to `0x1004`
* `numbers + 2` or `&numbers[2]` points to `0x1008`
* `numbers + 3` or `&numbers[3]` points to `0x100C`
* `numbers + 4` or `&numbers[4]` points to `0x1010`

### Example Code

```C
#include <stdio.h>

int main() {
  int numbers[5] = {1, 2, 3, 4, 5};

  // Accessing elements using array indexing
  printf("numbers[2] = %d\n", numbers[2]);  // Output: 3

  // Accessing elements using pointers
  printf("*(numbers + 2) = %d\n", *(numbers + 2));  // Output: 3

  // Pointer arithmetic
  int *ptr = numbers;
  printf("Pointer ptr points to numbers[0]: %d\n", *ptr);  // Output: 1
  ptr += 2;
  printf("Pointer ptr points to numbers[2]: %d\n", *ptr);  // Output: 3

  return 0;

```

# Multibyte Arrays

If we create an array of structs it gets cruzy because we can access and manipulate the elements using either indexing _or_ pointer arithmetic. Let's see how multi-byte width structures are managed in memory.

First, let's say we're working with our familiar Coordinate struct:

```C
typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;
```
We can declare an array of 3 `Coordinate` structs like so:
```C
coordinate_t points[3] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};
```
Then we can print out the values of the second element in the array:
```C
printf("points[1].x = %d, points[1].y = %d, points[1].z = %d\n",
  points[1].x, points[1].y, points[1].z
);

// points[1].x = 4, points[1].y = 5, points[1].z = 6
```
Or we can use a pointer:
```C
printf("ptr[1].x = %d, ptr[1].y = %d, ptr[1].z = %d\n",
  (ptr + 1)->x, (ptr + 1)->y, (ptr + 1)->z
);

// ptr[1].x = 4, ptr[1].y = 5, ptr[1].z = 6
```

### Memory Layout

Assuming each `int` is 4 bytes, the `Coordinate` structure will be 12 bytes (`3 * 4` bytes). Let's assume the `points` array starts at memory address `0x2000`


| Address | Element | Value | Offset (bytes) |
|:----:|:-------:|:-----:|:-----:|
| `0x2000` | `points[0].x` | 1 | 0 |
| `0x2004` | `points[0].y` | 2 | 4 |
| `0x2008` | `points[0].z` | 3 | 8 |
| `0x200C` | `points[1].x` | 4 | 12 |
| `0x2010` | `points[1].y` | 5 | 16 |
| `0x2014` | `points[1].z` | 6 | 20 |
| `0x2018` | `points[2].x` | 7 | 24 |
| `0x201C` | `points[2].y` | 8 | 28 |
| `0x2020` | `points[2].z` | 9 | 32 |

### Accessing Elements Using Pointers

  * `points + 0` or `&points[0]` points to `0x2000`
  * `points + 1` or `&points[1]` points to `0x200C` (next structure, offset by 12 bytes)
  * `points + 2` or `&points[2]` points to `0x2018`

# Array Casting

Let's explore a special kind of psychopathy that's possible in C. Let's assume we have this array of 3 structs where each struct holds 3 integers:
```C
coordinate_t points[3] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};
```
Because arrays are basically just pointers (in most cases; more on that later), and we know that structs are contiguous memory, we can cast the array of structs to an array of integers:
```C
int *points_start = (int *)points;
```
Then we can iterate over the known numbers of integers in the array of structs:
```C
for (int i = 0; i < 9; i++) {
  printf("points_start[%d] = %d\n", i , points_start[i]);
}
```
```C
// End of lesson .c file
#include "exercise.h"
#include <stdio.h>

void dump_graphics(graphics_t gsettings[10]) {
  int *ptr = (int *)gsettings;
  for (int i = 0; i < 30; i++) {
    printf("settings[%d] = %d\n", i, ptr[i]);
  }
}

// End of lesson .h file
typedef struct Graphics {
  int fps;
  int height;
  int width;
} graphics_t;

void dump_graphics(graphics_t gsettings[10]);

// End of lesson main.c file
#include "exercise.h"
#include "munit.h"

int main() {
  graphics_t graphics_array[10] = {
      {60, 1080, 1920},  {30, 720, 1280},  {144, 1440, 2560}, {75, 900, 1600},
      {120, 1080, 1920}, {60, 2160, 3840}, {240, 1080, 1920}, {60, 768, 1366},
      {165, 1440, 2560}, {90, 1200, 1920},
  };
  dump_graphics(graphics_array);
  return 0;
}
```

# Pointer Size

The size of an array depends on both the number of elements and the size of each element. An array is a contiguous block of memory where each element has a specific type, and therefore, a specific size.

In C, pointers are always the same size because they just represent memory addresses. The size of a pointer is determined by the architecture of the system. (e.g. 32-bit or 64-bit). A pointer's size doesn't depend on the type of data it points to; it just holds the address of a memory location.

### Pointer Example
```C
int *intPtr;
char *charPtr;
double *doublePtr;
printf("Size of int pointer: %zu bytes\n", sizeof(intPtr));
printf("Size of char pointer: %zu bytes\n", sizeof(charPtr));
printf("Size of double pointer: %zu bytes\n", sizeof(doublePtr));

// Size of int pointer: 4 bytes
// Size of char pointer: 4 bytes
// Size of double pointer: 4 bytes

```
In boot.dev's [WASM](https://webassembly.org/) environment, they're all the same [size](https://port70.net/~nsz/c/c11/n1570.html#6.5.3.4), because they're all just 32-bit memory addresses: it doesn't matter how much memory the value at that address takes up.

### Array Example
```C
int intArray[10];
char charArray[10];
double doubleArray[10];
printf("Size of int array: %zu bytes\n", sizeof(intArray));
printf("Size of char array: %zu bytes\n", sizeof(charArray));
printf("Size of double array: %zu bytes\n", sizeof(doubleArray));

// Size of int array: 40 bytes
// Size of char array: 10 bytes
// Size of double array: 80 bytes
```
Now the sizes are different because the array type keeps track of the size of each element and the number of elements. Although an array is a pointer to the first element, it's not _just_ a pointer: it's a block of memory that holds all the elements.
>[!NOTE]
> Boot.dev runs C in the browser using [WASM](), which is typically a 32-bit system. If you run this code on a 64-bit system, the size of the pointers will be 8 bytes.
