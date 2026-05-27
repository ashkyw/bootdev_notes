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

> [Information]
> The [`*p` format specifier](https://en.cppreference.com/w/c/io/fprintf#:~:text=The%20following%20format%20specifiers%20are%20available%3A) will format a pointer (memory address) to be printed.
