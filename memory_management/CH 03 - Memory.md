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
> The [`*p` format specifier](https://en.cppreference.com/w/c/io/fprintf#:~:text=The%20following%20format%20specifiers%20are%20available%3A) will format a pointer (memory address) to be printed.

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

  [!Alt Text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Memory%20-%20Virtual.png)

By only giving processes access to a chunk of virtual memory, the operating system can do some cool things:
  1. **Isolation**: One process can't access the memory of another process.
  2. **Security**: The OS can prevent processes from accessing certain parts of memory.
  3. **Simplicity**: Developers don't have to worry about managing physical memory of other processes.
  4. **Performance**: The OS can optimize memory access depending on the hardware and needs of the program. For example, by moving data between physical memory and the hard drive.

At the end of the day, your program has direct access to a virtual chunk of memory. Just like physical memory, it can be thought of as a big array of bytes, where each byte has an address.

# Pointers
