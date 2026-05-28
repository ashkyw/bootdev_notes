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


```
